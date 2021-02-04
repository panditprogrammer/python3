# input from user using numpy 
from numpy import *
a=int(input("Enter number of students :"))
b=zeros(a,dtype=int)
e=len(b)
c=0
while c<e:
	d=int(input("Enter "))
	b[c]=d
	c+=1
	
print( "total =",b)	