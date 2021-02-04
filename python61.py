#67..Comparing Numpy Arrays in Python
from numpy import *
a=array([11,10,13,14,15,18,14,18,29,20])
b=array([11,12,19,14,16,16,17,18,19,20])
c=b+1            # adding 1 in array b and assingning in c 

result = a==c
print( "**** ==*****",result)

result = a==b             # a equal b 
print(result)

result = a<c                #a less than c 
print( "<",result)
result = a>b               # a greater than b 
print(">",result)
result = a<=c                 # a less than equal c 
print(">=",result)
result = a>=b            # a greater than equal b 
print("<=",result)