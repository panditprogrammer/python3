# creating a tuple video164
# a=(1,2,3,4,5,7)
a=(1,20.8,-5,"panditprogrammer.com",5,7)
l=len(a)

print(a)
print(type(a))
# for i in range(l):
#     print(i,"index =",a[i])
i=0
while i<l:
    print(i,"index",a[i])
    i+=1
# slicing on tuple can be used to retriee a piece of the tuple that contains a group of
# elements .Slicing is useful to retrieve a range of elements.
# slc=a[0:4]
slc=a[2:5:2]
print("after slicing ",slc)