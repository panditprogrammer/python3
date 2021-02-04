#Getting input from user in set
a=set()
print(a)
n=int(input("Enter number of element"))
for i in range(n):
    a.add(input("Enter element"))
    print(a)

# copying elements of set using copy method
b=a.copy()
print(b)
print(id(a))
print(id(b))
# clearing all element in set using Clear met
# clear method
a.clear()
print(b)
print( "after",a)