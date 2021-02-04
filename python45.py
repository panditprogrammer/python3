#Append method in python using while loop
from array import *
a=array("i",[11,12,13,14,15,16,17,18,19,20])
b=len(a)
c=0
while c<b:
	print(c,"=",a[c])
	c+=1
a.append(int(input("Enter number :")))	
print(a)