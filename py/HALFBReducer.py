#!/usr/bin/python
import sys
from kernel import K
data_info = []
data_cluster = 0
#data_matrix = []
for datum in sys.stdin:
	datum = datum.strip().split()
	if int(datum[2]) == 0:
		data_info = [float(num) for num in datum[3:-1]]
		data_cluster = datum[-1]
		#data_matrix = [int(num) for num in datum[0:2]]
	elif int(datum[2]) == 1:
		info = [float(num) for num in datum[3:-1]]
		cluster = datum[-1]
		kernel = K(data_info, info)
		#matrix = [int(num) for num in datum[0:2]]
		print ''.join(str(f)+' ' for f in data_info) + cluster, kernel

 

"""
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
			print ''.join(f+' ' for f in feature) + str(cluster)+ ' B '+ str(-2*sum_number/cluster_count)
		except:
			pass
		cluster = int(xi_cluster)
		sum_number = 0
		cluster_count = 0
	sum_number = sum_number + float(xi_K)
	cluster_count = cluster_count + 1
	feature = xi_feature
print ''.join(f+' ' for f in feature)+ str(cluster), 'B', -2*sum_number/cluster_count"""
