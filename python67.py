# view method and copy method in array in python
from numpy import *
a=array([11,12,13,14])
b=a.view()
print(a, b)
print(type(b))
print("after modifying data in b"
)

a[2]=60
print(a,b)
c=copy(a)       # copy data a in to c 
print(c)
print(id(a))
#print(id(b))
print(id(c))
