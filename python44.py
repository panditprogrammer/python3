#Accessing Array using while loop 
from array import *
a=array("i",[11,12,13,14,15,16,17,18,19,20])
b=len(a)
c=0
print(" with index using while loop")
while c<10:
	print( c,"=",a[c])
	c+=1