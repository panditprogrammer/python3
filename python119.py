#  video  132  A list represent a group of elements
# List are very similar to array but there is major difference, an array can store only one type of elements whereas a list can store different type of
# of elements:
#     list are mutable  means we can modify it
a=[101,"panditprogrammer",30,50.2]
print(type(a),"\n",a)
print("This is length of list =",len(a))
for i in a:
    print(i)


# we can access using negative index
print("This is using negative index  at -2 ",a[-2])
print("This is using negative index  at -3 ",a[-3])
# we can modify using index
a[-1]="developer"
print(a)

# creating a empty list for getting value from user
b=[]

d=int(input("Enter number of element "))
for i in range(d):
    b.append(input("Enter elements for list "))


print(b)
print(type(b))