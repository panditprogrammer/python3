print("Maximum 10 character acceptable make sure you have Enter right ")

a=input("Enter your Name:")
b=len(a)
for x in range(b):
	print(x,"=",a[x])
	if x==10:
		break
