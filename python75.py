# reshape function in python 1D to 2D or 2D to 3D and so on
from numpy import *
a=array ([11,12,13,14,15,16,17,18,19,20])
d=reshape(a,(2,5)) 
#converting one dimension to multidimensional array in python

print("one to multi")
print(a)
print(d)
print("multi to one")
x=array([[11 ,12 ,13, 14 ,15],[16, 17, 18, 19, 20]])
y=x.flatten()   
 # flatten is used to coverting multi dimension to one
print(y)
