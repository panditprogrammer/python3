#Slicing in python 
from array import *
stu=array('i',[100,101,102,103,104,105])
n=len(stu)
for a in range(n):
    print(a, "=" ,stu[a])
    
print("after slicing ***********")
a=stu[1:5]
for b in a:
    print(b)
    
print("after slicing 2***********")
a=stu[1:5:2]
for b in a:
    print(b)
        