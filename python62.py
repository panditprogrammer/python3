#67..Comparing Numpy Arrays in Python size must be same 
from numpy import * 
a=array ([11,12,13,14,15,16,17,18,19,20])
b=array ([11,52,10,14,35,16,27,18,89,20])
c=a<b           # a less than b it returns True or False 
print(c)
c=a>b    
       # a greater than b it returns True or False 
print(c)
c=a==b   
        # a equal than b it returns True or False 
print(c)
c=a<=b           # a less than equal b it returns True or False 

print(c)
c=a>=b           # a greater than equal b it returns True or False 

print(c)