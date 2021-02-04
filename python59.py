#65.Numpy One Dimensional Array using ones Function in Python 
from numpy import *
a= ones(5) #default data type is float 
print(a)
n=len(a)
for b in range(n):
	print(b, "=",a[b])

