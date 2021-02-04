#Aliasing array in python
from numpy import *

a=array([11,12,13,14,15,16])
b=a
print(a)
print(type(a))
print(b)
print(id(a))
print(id(b))
print("both has same id in memory block")