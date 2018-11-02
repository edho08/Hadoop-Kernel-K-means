#!/usr/bin/python
def K(xi, xj):
	dot = [float(xi[i]) * float(xj[i]) for i in range(len(xi))]
	K = pow(sum(dot) + 0, 1)
	return K
