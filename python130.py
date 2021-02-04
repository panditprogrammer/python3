# higher order function
# map function in python
a=[11,22,33,44,55,66,77,88,99,100]

def fin1(n):

    return n+(n*10)


result=map(fin1,a)
print(result)
print(type(result))
l=list(result)
print(l)
for i in l:
    print(i)


