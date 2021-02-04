# list of tuple in python 179
a=[(1,3,4,7),(12,78,38)]
print(a)
print(id(a),type(a))
a.append((40,50,20))
print(a)
l=len(a)
for i in range(l):
    if type(a[i]) is tuple:
        l1=len(a[i])
        for j in range(l1):
            print(i,j,"index",a[i][j])
    else:
        print(i,"index",a[i])
