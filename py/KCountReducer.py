#!/usr/bin/python
#import sys
import sys


sum_cluster = 0
cluster = 0

for datum in sys.stdin:
	if int(datum) != cluster:
		print cluster, sum_cluster
		cluster = int(datum)
		sum_cluster = 0
	sum_cluster = sum_cluster +1
print cluster, sum_cluster
