#!/usr/bin/python
import sys
from kernel import K
data_info = []
data_cluster = 0
data_matrix = []
for datum in sys.stdin:
	datum = datum.strip().split()
	if int(datum[3]) == 0:
		data_info = [float(num) for num in datum[4:]]
		data_cluster = datum[0]
		data_matrix = [int(num) for num in datum[1:3]]
	elif int(datum[3]) == 1:
		info = [float(num) for num in datum[4:]]
		cluster = datum[0]
		kernel = K(data_info, info)
		matrix = [int(num) for num in datum[1:3]]
		print data_cluster, kernel
