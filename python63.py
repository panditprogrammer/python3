#68.any and all Functions in Python
from numpy import *
a=array([15,12,13,34,15])
c=array([15,12,13,34,15])
b=array([11,12,83,34,18])
print(any(a==b))  #any elements equal in array a and b, a==b its return True 
print(all(a==b))  #all elements equal in array a and b, a==b its return False 
print(all(a==c))  #all elements equal in array a and b, a==b its return False 