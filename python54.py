#Accessing array using while loop (numpy )
from numpy import *
a=array([11 ,12 ,13 ,14, 15 ,16, 17 ,18 ,19, 20])
print(type(a),a)
n=len(a)
b=0
while b<n:
	print(b,"index =",a[b])
	b+=1