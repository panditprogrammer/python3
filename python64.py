#69.where Function in Python 
from numpy import *
a=array([15,12,13,34,15])
c=array([15,12,13,34,15])
b=array([11,12,83,34,18])
d=where(a<b,a,b)
print(d)  #if a less than b then executed a else b executed 

d=where(a>b,a,b)
 
print(d)  #if a  greater than b then executed a else b executed 

d=where(a==b,a,b)

print(d)  #if a equal b then executed a else b executed 