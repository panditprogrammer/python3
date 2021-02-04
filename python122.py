#Slicing list in python
a=[51,52,53,54,55,56,57,58,59]
for i in a:
    print(i)

print("after slicing on list")
print("from 3 to 6")
b=a[3:6:]
print(b)
print("from 0 to 6th ")
b=a[:6:]
print(b)
print("from 0 to end")
b=a[:]
print(b)
print("from 3 to end")
b=a[3:]
print(b)
print('from -5 to -2')
b=a[-5:-2:]
print(b)


print("from 0 to end and stepsize")
b=a[0:7:2]
print(b)