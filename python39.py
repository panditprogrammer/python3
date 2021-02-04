#For loop in python 
Name= input("Enter Your Name :")
b=len(Name)
print("Your name contains " ,b ,"letters")
print("This is index of letters :")
for a in range(b):
	print(a ,"=" ,Name[a])