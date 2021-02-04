#      video 152A list within another list is called nested list
a=[1,2,3,4,5,[10,20,30,40],6,7,8,9,10]
print(a)
print(type(a))
b=len(a)
for i in range(b):
    if type(a[i]) is list:
        l=len(a[i])
        for j in range(l):
            print(i,j,"index =",a[i][j])

    else:
        print(i,"index =",a[i])
# print(a[5],a[2],a[7]) using index