#!/usr/bin/python
import sys
cluster = 1
cluster_count = 0
sum_number = 0
feature = []
for datum in sys.stdin:
	datum = datum.strip().split()
	xi_cluster = datum[-2]
	xi_K = datum[-1]
	xi_feature = datum[0:-2]

	if int(xi_cluster) != cluster:
		try:
			print ''.join(f+' ' for f in feature) + str(cluster), str(-2*sum_number/cluster_count)
		except:
			pass
		cluster = int(xi_cluster)
		sum_number = 0
		cluster_count = 0
	sum_number = sum_number + float(xi_K)
	cluster_count = cluster_count + 1
	feature = xi_feature
print ''.join(f+' ' for f in feature)+ str(cluster), -2*sum_number/cluster_count
