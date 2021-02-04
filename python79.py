# Attributes of Numpy Array
#size itemsize dtype nbytes 
from numpy import * 
a=array ([10,20,30,40,50,60,70,80,90])
b=array([[11,12,13,14,15,16,17,18,19],[21,22,23,24,25,26,27,28,29]])
print("1D array is dimension :", a.ndim)
print("2D array is dimension :" ,b.ndim)
# shape of nd array
print("\n")
print("shape of 1D array:", a.shape)
print("shape of 2D array :" ,b.shape)
# size of array nd array
print("\n")
print("size of 1D array ",a.size)
print("size of 2D array ",b.size)
# itemsize of nd array means size of memory block
print("\n")
print("itemsize of 1D array",a.itemsize)
print("itemsize of 2D array",b.itemsize)
# data type of nd array 
print("\n")
print("dtype of 1D array :",a.dtype)
print("dtype of 2D array :",b.dtype)
#nbytes of nd array how much consume memory by array
print("\n")
print("nbytes of 1D array :",a.nbytes)
print("nbytes of 2D array :",b.nbytes)