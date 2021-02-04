#accessing 2D array using while loop in python 
from numpy import *
a=ones((3,4),dtype=int)
print(a)
# accessing array using for loop
for x in a:
	for y in x:
		print(y)
	print("loop terminated here")	
	
	"""This is multiline comments in python"""
	
	
# with index ones function 
print("with index ones accessing")
n=len(a)
for x in range(n):
	m=len(a[x])
	for y in range(m):
		print("index", x,y,"=",a[x][y])