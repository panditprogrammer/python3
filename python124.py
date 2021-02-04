# copy method is used to copy all the elements of a list to another list.
a=[11,22,33,44,55,66,77,88,99]
b=a.copy()
print(b)
for i in b:
    print(i)

print(a)
print("after modifying b")
b[4]=500

print("a =",a)
print("b =",b)



#cloning list using " : "
print("after cloning e and a list ")
e=a[:]
print(e)
e[5]=300
print('a =',a)
print('e =',e)
