"""
Title     : Arrays
Subdomain : Numpy
Domain    : Python
"""
import numpy

ar = list(map(float, input().split()))
np_ar = numpy.array(ar, float)
print(np_ar[::-1])
