#insert method in array 
from array import *
stud=array('i',[100,101,102,])
n=len(stud)
i=0
while i<n:
    print(stud[i])
    i+=1
print ("array after insert method")
stud.insert(3,103)
stud.insert(4,104)
n=len(stud)
i=0
while (i<n):
        print(stud[i])
        i+=1