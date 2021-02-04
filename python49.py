#pop method in python 
from array import *
a=array('i',[11,12,13,14,15])
b=0
while b<len(a):
	print(a[b])
	b+=1
print("array after pop it will remove last element of array")
d=a.pop()
print(a)	
print(d)