#!/bin/bash
#Defining program variables
IP1="data/input1"
OP1="data/HALFCoutput"
CACHEFILE="data/KCount/KCountC#KCount"
MAPPER1="py/HALFCMapper.py"
REDUCER1="py/HALFCReducer.py"

echo 'Calculate C'
hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER1 \
-reducer $REDUCER1 \
-input $IP1 -output $OP1 \
-cacheFile $CACHEFILE

#!/bin/bash
#Defining program variables
IP2="data/HALFCoutput"
OP2="data/Coutput"
CACHEFILE="data/KCount/KCountC#KCount"
MAPPER2="py/CMapper.py"
REDUCER2="py/CReducer.py"

hadoop jar $HADOOP_JAR_PATH \
-mapper $MAPPER2 \
-reducer $REDUCER2 \
-input $IP2 -output $OP2

hadoop fs -getmerge $OP2"/" "Coutput"
hdfs dfs -put "Coutput" $OP2"/"
rm "Coutput"
