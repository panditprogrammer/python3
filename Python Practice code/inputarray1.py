#input array from user using while loop
#Getting input from User in Array using for loop
from array import *
stur=array('i',[])
n=int(input("Enter number of students"))
i=j=0
while i<n:
    stur.append(int(input("Enter  rolln.")))
    i+=1
while (j<len(stur)):
    print(stur[j])
    j+=1