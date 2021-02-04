#Getting input from user using while loop
from array import *
a= array('i',[])
n=int(input("Enter number:"))
b=0
while b<n:
	a.append(int(input("Enter roll. ")))
	b+=1
print(a)	

d=0
while d<len(a):
	
	print(a[d])	
	d+=1