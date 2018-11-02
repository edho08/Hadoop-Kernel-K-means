#!/usr/bin/python
#import sys
import sys

for datum in sys.stdin:
	datum = datum.strip().split()
	cluster = int(datum[-1])
	print 0
	print cluster
