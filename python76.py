# input from user using for loop in multi dimensional array in python
from numpy import * # This is 81st video 
#a=zeros((2,3),dtype=int
a=int(input( "Enter number of rows :"))
b=int(input( "Enter number of coloum :"))
c=zeros((a,b),dtype=int)
#print(c ,"\n",c.dtype)
d=len(c)
for e in range(d):
	for f in range(len(c[e])):
		c[e][f]=int(input("Enter elements .."))

print(c)		            
for e in range(d):   
#for loop for printing with index array
	for f in range(len(c[e])):
		print( e,f,"index",c[e][f])
