from sys import  *
# important function id()
# This function return the "indentity" of an object it is not a addressa
a=20
b=30
c=a*b
print(c,id(c))
d=[10,30,70,73,38]
print(id(d))


# important function getsizeof()
# This function return the "size" of an object

print(getsizeof(d))
print(getsizeof(a,b))


# important function type()
# This function return the "type " of an object
print(type(a))
print(type(d))