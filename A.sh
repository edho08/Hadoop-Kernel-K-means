#!/bin/bash
#Defining program variables
IP="data/input1"
OP="data/Tinput/Aoutput"
MAPPER="py/AMapper.py"
REDUCER=""

echo 'Calculate A'
hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER \
-input $IP -output $OP
