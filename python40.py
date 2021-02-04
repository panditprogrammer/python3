#break  and continue statements in python
b=int(input("Enter a number under 100 :"))
for a in range(100):
	if a==0:
		continue
	print(a)	
	if(a==b):
		break