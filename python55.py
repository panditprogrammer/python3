#Creating array using linspace() Function (numpy )
from numpy import *
#a=array([11 ,12 ,13 ,14, 15 ,16, 17 ,18 ,19, 20])
a=linspace(1,20,5,endpoint=False)
print(type(a), a)
a[2]=23
print(a)
b=0
for b in a:
	print(b)
	