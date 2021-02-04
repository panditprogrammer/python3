#Accessing list using for loop
"""a=[10,20,30,40,50,60,70,90,80,100]
print(type(a))
for i in a:
    print(i)

print("rest of the code")

# with index

for i in range(len(a)):

    print(i,"=",a[i])


print("rest of the code")

#Accessing list using while loop
print("this is accessing using while loop")
b=["chandan",10,20.8,'ara',0.777]
i=0
while i<len(b):
    print(i,"=",b[i])
    i+=1

print("rest of the code")
"""
# creating a empty list and getting input from user
d=[]
nm=int(input("Enter number of element"))
for i in range(nm):
    d.append(input("Enter element") )

print(d)
j=0
while j<nm:
    print(j,"=",d[j])
    j+=1