#!/usr/bin/python
#get kernel
#from kernel import K
import sys

index = 0
	
#open cache (cache is just data)
f = open('KCount', 'r')
C = {}
for datum in f:
	datum = datum.strip().split()
	xi_cluster = datum[0]
	xi_value = datum[1]
	C[int(xi_cluster)] = int(xi_value)

for datum in sys.stdin:
	datum = datum.strip().split()
	#seperate features and cluster
	xi_features = datum[0:-1]
	xi_cluster = datum[-1]
	for i in range(0,C[0]):
		print str(index), str(i),0, ''.join(f+' ' for f in xi_features) + xi_cluster
		print str(i), str(index),1,''.join(f+' ' for f in xi_features) + xi_cluster
	index = index + 1


	
