# Multidimensional array in python using numpy
from numpy import *
a= array([[11,12,13,14,15],[16,17,18,19,20.]])
print(type(a))
print(a.dtype)
for b in a:           # accessing 2d array in python                  using           for loop
	for c in b:
		print(c)
	print("loop terminate here")	
