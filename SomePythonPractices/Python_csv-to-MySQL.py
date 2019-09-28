"""
@author: Jerry Junqi Yang
"""
"""
    Use PyMySQL to connect to MySQL
    Use csv to process our csv file
"""
import pymysql
import csv

# DB parametres
config = {'host':'',
          'port':3306,
          'user':'root',
          'passwd':'',
          'charset':'utf8mb4',
          'local_infile':1,
          'db':''
          }

conn = pymysql.connect(**config)
cur = conn.cursor()

csv_file = open("contact_list.csv")
headers = csv_file.readline() # Get the property(header) of each column

reader = csv.reader(csv_file)

for row in reader:
    
    business = row[0]
    title = row[1]
    firstname = row[2]
    lastname = row[3]
    dob = row[4]
    street1 = row[5]
    street2 = row[6]
    suburb = row[7]
    city = row[8]
    postcode = row[9]
    home_number = row[10]
    fax_number = row[11]
    work_number = row[12]
    mobile = row[13]
    other = row[14]
    notes = row[15]
    
    sql = "INSERT INTO `contact` (`title`, `first_name`, `last_name`, \
                                  `company_name`, `date_of_birth`, `notes`) \
                                   VALUES (%s, %s, %s, %s, %s, %s)"
    
    title = title.strip() # Remove Space
    title = title.strip(".") # Remove '.' in the csv file
    title = title.title() # Capitalize
    firstname = firstname.title()
    lastname = lastname.title()
    business = business.title()
    
    # Missing Values
    if title == "":
        title = None
    if firstname == "":
        firstname = None
    if lastname == "":
        lastname = None
    
    # Date of Birth
    # Or use re.split() for complex use. E.g. re.split(r'[;,\s]\s*', string)
    if "-" in dob:
        arr = dob.split("-")
    else:
        arr = dob.split("/")
    if len(arr) != 3:
        dob = None
    else:
        month = arr[0]
        day = arr[1]
        year = arr[2]
        if len(year) == 2: 
            year = "19" + year
        dob = "%s-%s-%s" % (year, month, day)
    cur.execute(sql, (title, firstname, lastname, business, dob, notes))
    contact_id = conn.insert_id() # Obtain the PK id while inserting
    conn.commit()

    name = ""
    if firstname is not None:
        name = firstname
    if lastname is not None:
        name = name  + lastname
    if name  == "":
        name = None
        
    # Deal with the Prefixes
    # Use startswith() to check our data
    if not mobile.startswith("64"):
        mobile = "64" + mobile
    if not home_number.startswith("09"):
        home_number = "09" + home_number
    if not work_number.startswith("09"):
        work_number = "09" + work_number
    if not other.startswith("09"):
        other = "09" + other
    
    sql = "INSERT INTO `address` (`contact_id`,`street1`, `street2`, \
                                  `suburb`,`city`, `post_code`) \
                                  VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (contact_id, street1, street2, suburb, city, postcode))
    conn.commit()
    sql = "INSERT INTO `phone` (`contact_id`,`name`, `content`, `type`) \
                                  VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (contact_id, name, home_number, "Home"))
    conn.commit()
    sql = "INSERT INTO `phone` (`contact_id`,`name`, `content`, `type`) \
                                  VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (contact_id,name, work_number, "Work"))
    conn.commit()
    sql = "INSERT INTO `phone` (`contact_id`,`name`, `content`, `type`) \
                                  VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (contact_id, name, mobile, "Mobile"))
    conn.commit()
    sql = "INSERT INTO `phone` (`contact_id`,`name`, `content`, `type`) \
                                  VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (contact_id, name, other, "Other"))
    conn.commit()

# Close Connection
conn.close()