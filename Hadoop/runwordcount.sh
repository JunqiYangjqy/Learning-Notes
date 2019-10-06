#!/bin/bash/
 
 hadoop fs -rm -r -f /''address''/wordcount
 
 hadoop jar /hadoop-streaming.jar \ #file path of streaming.jar
 -libjars /opt/lib/hive/lib/hive-exec-1.1.0-cdh5.4.8.jar \
 -jobconf mapreduce.reduce.shuffle.memory.limit.percent=0.1 \
 -jobconf mapreduce.reduce.shuffle.input.buffer.percent=0.3 \
 -jobconf mapreduce.map.memory.mb=512 \
 -jobconf mapreduce.reduce.memory.mb=512 \
 -jobconf mapred.map.capacity=100 \
 -jobconf mapred.reduce.capacity=100 \
 -jobconf mapred.job.name=test_word_count \
 -file mapper.py \
 -file reducer.py \
 -mapper "python mapper.py" \
 -reducer "python reducer.py" \
 -input /hive/words \
 -output /hive/wordcount \

 #hadoop fs -getmerge /''address''/wordcount wordcount