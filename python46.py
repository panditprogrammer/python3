#Getting input from user using for loop
from array import *
a=array("i",[])
c=int(input("Enter number:"))
for d in range(c):
	a.append(int(input("Enter roll no." )))

e=len(a)
for f in range(e):
	print(f,"=",a[f])
