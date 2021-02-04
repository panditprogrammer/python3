#Accessing array in python using logspace() function
from numpy import *
a=logspace(1,3,5)
print( a ,type(a))
n=len(a)
for b in range(n):
	print(b,"index",a[b])
	
