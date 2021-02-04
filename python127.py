#passing a list in function in python
# returning a list from function video155
def fuc1(l1):
    print(l1)
    print(type(l1))
    for i in l1:
        print(i)
    l1.append(11)
    return l1

a=[12,13,14,15,16,17,18,19,20]
rl=fuc1(a)
print( "returned list",rl)
