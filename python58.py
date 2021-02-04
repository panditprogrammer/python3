# one dimensional array zeros () funtion 
from numpy import *
a= zeros(5,dtype=int) # default data type is float 
n=len(a)
for b in range(n):
	print(b,"=",a[b])
	
print(type(a))	
