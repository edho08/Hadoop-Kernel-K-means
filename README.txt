1. SET config on config.sh
2. Put your input file in hdfs
2.1 File format is CSV like file without any string (encoded)
3. to run program, run kmeans.sh
4. Change the Kernel by changing py/kernel.py 
(yes i know you need to change the code.. which is bad) 


NOTE!!:
1. Not tested yet, especially on multi-node hadoop set up.
2. This program use Hadoop distributed cache which is deprecated.
3. This program use hadoop fs -getmerge which (might be) is deprecated.
4. No error handling.
5. Use at your own risk.




edho08@gmail.com (personal)
edho08@student.ub.ac.id (work & school related)
FILKOM
UNIVERSITAS BRAWIJAYA
2018 
