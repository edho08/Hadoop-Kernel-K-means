#!/usr/bin/python

import sys
# get kernel
from kernel import K

# read data
for datum in sys.stdin:
	datum = datum.strip().split()
	#split data cluster and features
	features = datum[0:-1]
	cluster = datum[-1]
	#K(xi, xi)
	kernel = K(features, features)
	#MAP <features, (cluster (0), A, K(xi,xi))>
	print ''.join(f+' ' for f in features)+ str(0) , str(kernel)
