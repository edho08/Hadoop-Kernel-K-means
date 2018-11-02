#!/usr/bin/python

import sys

cluster_size = int(sys.argv[1])
c = 1 
index = 1

# Read data

for datum in sys.stdin:
	datum = datum.strip().split(',')
	datum = [float(num) for num in datum]
	print ''.join(str(f)+' ' for f in datum) + str(c)
	c = c+1 if c<cluster_size else 1
	index = index+1
