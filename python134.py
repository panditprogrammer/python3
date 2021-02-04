# '+' is used to do concatenation of tuple
a=tuple(range(12,20))
b=tuple(range(20,200,34))
print(a,type(a))
print(b,type(b))
print("after concate")
c=a+b
print(c)
# tuples elements are immutable so it is not possible to modify, update or delete is's elemtnt
#we can modify like this ...
a1=(12, 13, 14, 15, 16, 17, 18, 19)

# s1=a[:4]
# s2=b[4:]
# s=(100,200)
# tuple1=s1+s+s2
# print(tuple1)
# deleting a tuple without modified
# del a1
print(a1)
s1=a1[:4]
s2=a1[5:]
t=s1+s2
print(t)
print(id(t))
print(id(a1))