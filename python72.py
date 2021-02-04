# creating 2D array using zeros ()Function
from numpy import *
a=zeros((2,3) ,dtype=int)
print(a)
print("This is lenth of a is ",len(a))
n=len(a)
for b in range(n):  
 # range for index like 0,1,in case of range 2.
	m=len(a[b])
	print("This is a lenth of a[b]",m)
	for c in range(m):
		#print("This is inner for loop")
		print( b,c,"index =",a[b][c])
			