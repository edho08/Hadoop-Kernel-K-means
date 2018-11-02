#!/bin/bash
#Defining program variables
IP=$INPUT
OP="data/input1"
MAPPER="py/setupMapper.py $CLUSTERNUM"
REDUCER=""

echo 'Commencing SETUP'
hadoop jar $HADOOP_JAR_PATH \
-mapper "$MAPPER" \
-input $IP -output $OP

