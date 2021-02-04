#Accessing two dimensional array in python using while loop
from numpy import *
a=array([[10,11,12,13,14,15],[21,22,23,24,25,26]])

b=0

n=len(a)

while b < n:
	c=0
	while c < len(a[b]):
	
		print(a[b][c])
		
		c+=1
		
	b+=1
	print("main loop ")