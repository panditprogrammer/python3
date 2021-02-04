#Append() method in array
from array import *
stur=array("i",[100,101,102,103,104,105])
n=len(stur)
i=0
while (i<n):
	print(stur[i])
	i+=1
print("after append array in like this ")
stur.append(107)  
stur.append(106)
n=len(stur)
i=0
while (i<n):
	print(stur[i])
	i+=1