#arange function in python using while loop
from numpy import *
a=arange(1,10)
print(type(a))
n=len(a) #to find lenth of "a" using len function
print(a)
b=0
print("*********while loop ***********")
while b<n:
	print(b,"index",a[b])
	b+=1 
print("********* for  loop *****")	
for c in range(n):
	print(c ,"index",a[c])