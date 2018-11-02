#!/usr/bin/python
import sys
cluster = 1
cluster_count = 0
sum_number = 0
for datum in sys.stdin:
	try:	
		datum = datum.strip().split()
		xi_cluster = datum[0]
		xi_K = datum[1]
		if int(xi_cluster) != cluster:
			try:
				print str(cluster), str(sum_number/cluster_count)
			except:
				pass
			cluster = int(xi_cluster)
			sum_number = 0
			cluster_count = 0
		sum_number = sum_number + float(xi_K)
		cluster_count = cluster_count + 1
	except:
		pass
print cluster, sum_number/cluster_count
