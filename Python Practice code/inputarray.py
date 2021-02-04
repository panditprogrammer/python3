#Getting input from User in Array using for loop
from array import *
stur=array('i',[])
n=int(input("Enter number of students"))
m=range(n)
for i in m:
    stur.append(int(input("Enter  rolln.")))
for i in m:
    print(stur[i])