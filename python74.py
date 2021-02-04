#accessing 2D array using while loop in python 
from numpy import *
a=ones((3,4),dtype=int)
print(a)
n=0
print("lenth is ",len(a))
while n < len(a):
	m=0
	while m < len(a[n]):
		print( "index ",n,m,"=",a[n][m])
		m+=1
	
	n+=1
		
	print("loop terminated here")	