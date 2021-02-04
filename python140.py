#tuple of list in python
a=([12,13,17],[10,20,30])
print(a,type(a))
t=type(a[0]) is list
print(t)
a[0][0]=5
print(a)
n=len(a)
for i in range(n):
    if type(a[i]) is list:
        print(i,"index",a[i])
        l1=len(a[i])
        for j in range(l1):
            print(i,j,"index",a[i][j])
    else:
        print(i,"index",a[i])
