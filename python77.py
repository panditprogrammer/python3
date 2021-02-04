# input from user in multi dimensional array using while loop in python
from numpy import *
#video no.82
a=int(input("Enter number of classes :"))
b=int(input("Enter number of students in each class :"))
arr1=zeros((a,b),dtype=int)
# print(arr1)
c=len(arr1)
print(c)
print("using while loop ")
d=0
while d<c:
	e=0
	while e< len(arr1[d]):
		print(arr1[d],"next...") 
		#first row is here
		arr1[d][e]=int(input("Enter elements.."))
		e+=1
	d+=1
print(arr1)	
print("with index all data is here")
d=0
while d<c:
	e=0
	while e< len(arr1[d]):
		print( d,e,"index",arr1[d][e])
		e+=1
	d+=1	