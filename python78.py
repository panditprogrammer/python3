# slicing array in multi dimensional array in python 
#video 83\
from numpy import *
# a=array([[11,13,17],
		 # [11,12,13],
		 # [21,22,23]	])
# print("array after printing")
# print(a)
# print("1st row 2nd coloum")
# b=a[1,2 ]
# print(b)
# print("2nd coloum")
# c=a[0:1,0:1]
# print(c)
x=array ([

        [1,2,3,4,5,],
		[11,12,13,14,15],
		[21,22,23,24,25],
		                   ])
						
print(x)	
print("0th row and all coloum\n")
n=x[ 0, : ]	

print(n)
print("1th row and all coloum\n")
n=x[ 1, : ]	

print(n)
print("2nd row and all coloum\n")
n=x[ 2, : ]	
print(n)
print("0th coloum and all rows\n")
n=x[ :, 0 ]	

print(n)
print("1st coloum and all rows \n")
n=x[ :, 1 ]	
print(n)
print("2nd coloum and all rows\n")
n=x[ :, 2]	
print(n)	
print("3rd coloum and all rows\n")
n=x[ :, 3]	
print(n)
print("4th coloum and all rows\n")
n=x[ :, 4]	
print(n)			