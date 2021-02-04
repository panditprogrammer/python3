# extend method in python
from array import *
stu=array('i',[101,102,103,104,105])
ar=array ('i',[106,107,108])
n=len(stu)
i=0
while(i<n):
    print(stu[i])
    i+=1
    
print("Array After Extend")
stu.extend(ar)
n=len(stu)
i=0
while(i<n):
    print(stu[i])
    i+=1    