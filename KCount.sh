#!/bin/bash
#Defining program variables
IP="data/input1"
OP="data/KCount"
MAPPER="py/KCountMapper.py"
REDUCER="py/KCountReducer.py"

hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER \
-reducer $REDUCER \
-input $IP -output $OP

hadoop fs -getmerge $OP"/" "KCount"
hdfs dfs -put "KCount" $OP"/KCountB" &
hdfs dfs -put "KCount" $OP"/KCountC" &
wait
rm "KCount"
