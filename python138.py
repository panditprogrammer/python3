# passing a tuple in function in python
# returning a tuple from function video178

def fuc1(n):
    print(n)
    for i in n:
        print(i)
    print(type(n))
    b=(12,87)
    return n+b

a=(1,20,23,87)
s=fuc1(a)
print(s)
for i in s:
    print(i)
print(type(s))

