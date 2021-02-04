# passing a set into a function video 190
a={10,29,80,83,74,47}

def fun1(x):
    for i in x:
        print(i)
    print(x,type(x))
    x.add(100)
    return x

s=fun1(a)
print(s)
print("rest of the code")