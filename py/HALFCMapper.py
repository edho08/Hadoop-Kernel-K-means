#!/usr/bin/python
#get kernel
#from kernel import K
import sys


#open cache (cache is just data)
f = open('KCount', 'r')
C = {}
index = {}
for datum in f:
	datum = datum.strip().split()
	xi_cluster = datum[0]
	xi_value = datum[1]
	C[int(xi_cluster)] = int(xi_value)
	index[int(xi_cluster)] = 0	



for datum in sys.stdin:
	datum = datum.strip().split()
	#seperate features and cluster
	xi_features = datum[0:-1]
	xi_cluster = int(datum[-1])
	for i in range(0,C[xi_cluster]):
		print  str(xi_cluster), str(index[xi_cluster]), str(i),0, ''.join(f+' ' for f in xi_features)
		print str(xi_cluster), str(i), str(index[xi_cluster]),1,''.join(f+' ' for f in xi_features)
	index[xi_cluster] = index[xi_cluster] + 1


	
