#array using numpy in python
from numpy import *
a=array([11,12,13,14,15,16,17,18,19,20]) #this is numpy array
print(type(a), a)
n=len(a)
for b in range(n):
	print(b,"=",a[b])
	b+=1