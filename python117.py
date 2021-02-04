#Passing and Returning Numpy array in python
from array import *
def numi(x):
    print("This is array")
    print(x)
    print("after appending ")
    x.append(1111)
    return x

arr1=array('i',[21,22,23,24,25])
a=numi(arr1)
print(a)
print(type(a))
p=len(a)  # This is for getting lenth of
for i in range(p):   # range for getting index 
    print(i," index =",a[i])