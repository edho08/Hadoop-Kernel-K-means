./banner.sh
. ./config.sh
hdfs dfs -rm -r "data" &
hdfs dfs -rm -r $OUTPUT
./setup.sh
for i in $(seq 1 $ITER) 
do
echo "<<<<<<<<<<<iter-"$i"->>>>>>>>>>>>>"
./iter.sh
./clear.sh
done
./output.sh
