#pop method in array python
from array import *
stud=('i',[101, 102,103, 104])
n=len(stud)
i=0
while (i<n):
    print(stud[i])
    i+=1
print("array after pop")
t=stud.pop(1)
print(t)
n=len(stud)
i=0
while (i<n):
    print(stud[i])
    i+=1