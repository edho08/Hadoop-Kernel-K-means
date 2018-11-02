#!/bin/bash
#Defining program variables
IP="data/Tinput/*/*"
OP="data/Total"
MAPPER="py/TotalMapper.py"
REDUCER="py/TotalReducer.py"
CACHEFILE="data/Coutput/Coutput#Coutput"

echo 'Calculating Cluster Member'
hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER \
-reducer $REDUCER \
-cacheFile $CACHEFILE \
-input $IP -output $OP

hdfs dfs -rm -r "data/input1"
hdfs dfs -mv $OP "data/input1"

