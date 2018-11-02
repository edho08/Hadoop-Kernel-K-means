#!/bin/bash
#Defining program variables
IP1="data/input1"
OP1="data/HALFBoutput"
CACHEFILE="data/KCount/KCountB#KCount"
MAPPER1="py/HALFBMapper.py"
REDUCER1="py/HALFBReducer.py"

echo 'Calculate B'
hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER1 \
-reducer $REDUCER1 \
-input $IP1 -output $OP1 \
-cacheFile $CACHEFILE

#Defining program variables
IP2="data/HALFBoutput"
OP2="data/Tinput/Boutput"
CACHEFILE="data/KCount/KCountB#KCount"
MAPPER2="py/BMapper.py"
REDUCER2="py/BReducer.py"

hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER2 \
-reducer $REDUCER2 \
-input $IP2 -output $OP2 \

