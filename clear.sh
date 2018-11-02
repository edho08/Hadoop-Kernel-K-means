#!/bin/bash
#cleaning garbage
echo "cleaning garbage!!!"
hdfs dfs -rm -r "data/KCount" &
hdfs dfs -rm -r "data/Tinput" &
hdfs dfs -rm -r "data/Coutput" &
hdfs dfs -rm -r "data/HALFBoutput" &
hdfs dfs -rm -r "data/HALFCoutput" &
wait
