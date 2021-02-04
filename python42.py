#Array in pyhon one dimensional array input from user to extend array

from array import *
a= array('i',[11,12,13,14,15,16,17,18,19,20])
print( type(a))
for b in a:
	print(b)
a.append(int(input()))	
print(a)