#pop method in python in array for removing last array's element or particular element
from array import * 
stud=('i',[100,101,102,103,104,105])
n=len(stud)
i=0
while i<n:
	print(stud[i])
	i+=1
print('from here is pop method')
stud.pop(1)# line 10 has a error be carefull
a=len(stud)
i=0
while i<n:
	print(stud[i])
	i+=1	

