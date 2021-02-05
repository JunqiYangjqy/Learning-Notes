# Author: Jerry
# Date: 2020-11-20

# Some Glue related functions

def export_table_partition_info(source_table, export_location=None):
    source_db_name, source_tbl_name = source_table.split('.')
    source_tbl_glue_partition = glue_client.get_table(
        DatabaseName=source_db_name,
        Name=source_tbl_name,
    )['Table']

    source_partition_columns = [c['Name'] for c in source_tbl_glue_partition['PartitionKeys']]
    partition_values = all_partitions_from_index(
        index_table=source_table,
        partition_columns=source_partition_columns,
    )(athena=athena)['data']
    # Get all the partitions from source_table
    partition_values = partition_to_string(partition_values)
    partition_values = list(
        map(list, partition_values),
    )  # [list(partition) for partition in partition_values]
    # print("partition_values",partition_values)

    batch_partitions_to_get = [
        partition_values[idx : idx + 100] for idx in range(0, len(partition_values), 100)
    ]
    if export_location == None:
        import os

        export_location = os.getcwd()
    with open(
        f'{export_location}/{source_db_name}_{source_tbl_name}_partitions_info.json',
        'w',
    ) as f:
        for partitions in batch_partitions_to_get:
            if isinstance(partitions[0], list):
                partition_values_to_get = [{'Values': partition} for partition in partitions]
            else:
                partition_values_to_get = [{'Values': [partition]} for partition in partitions]

            source_partition_info = glue_client.batch_get_partition(
                DatabaseName=source_db_name,
                TableName=source_tbl_name,
                PartitionsToGet=partition_values_to_get,
            )['Partitions']
            for i in source_partition_info:
                # print("This is i: ", i)
                i.pop('CreationTime', '')
                i.pop('LastAccessTime', '')
                i.pop('LastAnalyzedTime', '')
            jsObj = json.dumps(source_partition_info)
            f.write(jsObj)

    # print("all_partition_info: ",all_partition_info)
    # print("length",len(all_partition_info))
    # print("all_partition_info[0]",all_partition_info[0][0]['Parameters'])

def glue_partition_remapping(source_table, target_table, partition_values=None):
    """
    Use this function to remap partitions from one table to another (when rebuilding)
    """
    source_db_name, source_tbl_name = database_table_split(source_table)
    target_db_name, target_tbl_name = database_table_split(target_table)

    # target table is the table you will be mapping to (you'll give partitions to)
    # i.e. the final table you want, such as choice_transactions
    target_glue_table = glue_client.get_table(
        DatabaseName=target_db_name,
        Name=target_tbl_name,
    )
    target_glue_table_sd = target_glue_table['Table']['StorageDescriptor']

    # source table is the table we used to map from, i.e. the table we rebuild and named such as choice_transacitons_tmp
    source_glue_table = glue_client.get_table(
        DatabaseName=source_db_name,
        Name=source_tbl_name,
    )
    source_glue_table_sd = source_glue_table['Table']['StorageDescriptor']

    # To get the partition columns from source table
    target_tbl_glue_partition = glue_client.get_table(
        DatabaseName=target_db_name,
        Name=target_tbl_name,
    )['Table']
    target_partition_columns = [c['Name'] for c in target_tbl_glue_partition['PartitionKeys']]
    print(f"target table {target_table} partition_columns", target_partition_columns)

    source_tbl_glue_partition = glue_client.get_table(
        DatabaseName=source_db_name,
        Name=source_tbl_name,
    )['Table']
    source_partition_columns = [c['Name'] for c in source_tbl_glue_partition['PartitionKeys']]
    print(f"source table {source_table} partition_columns are: ", source_partition_columns)
    if target_partition_columns != source_partition_columns:
        raise Exception("Source table & Target table partition columns don't match, please check")

    # delete existing partition first in target table - just to be safe
    while True:
        target_existing_partitions = glue_client.get_partitions(
            DatabaseName=target_db_name,
            TableName=target_tbl_name,
        )['Partitions']
        if target_existing_partitions == []:
            print("No partition in target table needs to delete")
            break
        partition_values_to_del = [partition_del['Values'] for partition_del in target_existing_partitions]
        print("Existing Partitions in target table will be deleted are: ", partition_values_to_del)
        batch_partitions_to_delete = [
            partition_values_to_del[idx : idx + 24] for idx in range(0, len(partition_values_to_del), 24)
        ]
        for partitions_to_delete in batch_partitions_to_delete:
            partitions_del_batch = [{'Values': partition_del} for partition_del in partitions_to_delete]
            # print("partitions_del_batch",partitions_del_batch)
            glue_client.batch_delete_partition(
                DatabaseName=target_db_name,
                TableName=target_tbl_name,
                PartitionsToDelete=partitions_del_batch,
            )

    source_table_loc = source_tbl_glue_partition['StorageDescriptor']['Location']
    source_table_loc_components = urlparse(source_table_loc)
    source_table_bucket = source_table_loc_components.netloc
    source_table_prefix = source_table_loc_components.path.lstrip('/')

    # Get table bucket and prefix/path get the path from target table
    table_loc = target_tbl_glue_partition['StorageDescriptor']['Location']
    table_loc_components = urlparse(table_loc)
    table_bucket = table_loc_components.netloc
    table_prefix = table_loc_components.path.lstrip('/')

    # if partition_values is not provided, then we get all partition values from the source table
    if not partition_values:
        partition_values = all_partitions_from_index(
            index_table=source_table,
            partition_columns=source_partition_columns,
        )(athena=athena)['data']
        # Get all the partitions from source_table
        partition_values = partition_to_string(partition_values)
    partition_values = list(
        map(list, partition_values),
    )  # [list(partition) for partition in partition_values]
    print("partition_values", partition_values)
    batch_partitions_to_create = [
        partition_values[idx : idx + 100] for idx in range(0, len(partition_values), 100)
    ]

    for partitions in batch_partitions_to_create:
        # Generate path info for partitions
        if isinstance(partitions[0], list):
            partition_values_to_get = [{'Values': partition} for partition in partitions]
        else:
            partition_values_to_get = [{'Values': [partition]} for partition in partitions]

        source_partition_locs = glue_client.batch_get_partition(
            DatabaseName=source_db_name,
            TableName=source_tbl_name,
            PartitionsToGet=partition_values_to_get,
        )['Partitions']

        source_partitions_loc_suffix = [
            i['StorageDescriptor']['Location'].split(source_table_prefix)[1] for i in source_partition_locs
        ]
        s3_prefix_path = [
            's3://%s/%s%s' % (table_bucket, table_prefix, partition_component)
            for partition_component in source_partitions_loc_suffix
        ]
        # update the partition glue storagedescriptor info using the current table info except for the 'Location' part
        sd = [
            {
                'Columns': target_glue_table_sd['Columns'],
                'Location': path,
                'InputFormat': target_glue_table_sd['InputFormat'],
                'OutputFormat': target_glue_table_sd['OutputFormat'],
                'Compressed': target_glue_table_sd['Compressed'],
                'SerdeInfo': target_glue_table_sd['SerdeInfo'],
            }
            for path in s3_prefix_path
        ]

        partition_values_to_create = [
            {
                'Values': partition_value,
                'StorageDescriptor': sd[index],
                'Parameters': {'last_modified': str(time.time())},
            }
            for index, partition_value in enumerate(partitions)
        ]
        print("partition_values_to_create", partition_values_to_create)
        try:
            glue_client.batch_create_partition(
                DatabaseName=target_db_name,
                TableName=target_tbl_name,
                PartitionInputList=partition_values_to_create,
            )
        except ClientError as ex:
            if ex.response['Error']['Code'] != 'AlreadyExistsException':
                raise ex
            logging.info('Error occured when calling batch_create_partition().')