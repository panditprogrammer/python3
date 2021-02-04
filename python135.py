#  video 170 creating a list and getting input from user and convert into a tuple
a=[]
n=int(input("Enter number of elements "))
for i in range(n):
    a.append(int(input("Enter element")))

print(type(a))
a=tuple(a)
print(a)
print(type(a))
# repeatition of tuple using * operator
a=a*2
print(a)
#aliasing a tuple means giving a another name to the existing object. It dones't mean copying
b=a
print(b,type(b),id(b),id(a))
