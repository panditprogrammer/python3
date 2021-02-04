# slicing on array in python 
from array import *
a=array('i',[11,12,13,14,15,16,17,18])
print(a)
n=len(a)
for b in range(n):
	print(b,"=",a[b])
	
print("after slicing ")

a1=a[1:5]
for b in a1:
	print(b)
print(a1)	
