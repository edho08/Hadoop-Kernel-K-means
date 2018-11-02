#!/usr/bin/python
import sys
import math

min_num = float("inf")
arg_min = 0
index = 0
A = 0
C ={}
f = open('Coutput', 'r')
first = True
feature = []
for datum in f:
	datum = datum.strip().split()
	xi_cluster = datum[0]
	xi_value = datum[1]
	C[int(xi_cluster)] = float(xi_value)
for datum in sys.stdin:
	datum = datum.strip().split()
	xi_cluster = datum[-2]
	xi_value = datum[-1]
	xi_feature = datum[0:-2]
	if xi_cluster == str(0) and not first:
		A = xi_value
		print ''.join(f+' ' for f in feature)+str(arg_min)
		feature = xi_feature
		arg_min = 0
		min_num = float('inf')
	elif first:
		
		first = False
		A = xi_value
		feature = xi_feature
		arg_min = 0
		min_num = float('inf')
	else:
		ABC = float(A) + float(xi_value) + C[int(xi_cluster)]
		#print ''.join(f+' ' for f in feature)+str(xi_cluster), ABC
		if ABC < min_num:
			arg_min = xi_cluster
			min_num = ABC	
print ''.join(f+' ' for f in feature)+str(arg_min)
