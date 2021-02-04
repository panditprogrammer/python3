# Accessing nested dictionary using for loop in python
a={'course': 'python', 'fee': 50000, 1: {'couse': 'java', 'fee': 20000, 'course1': 'c/c++'}}
# for i in a:
#     print(i,"=",a[i])
#     if type(a[i]) is dict:
#         for j in a[i]:
#             print(j,"=",a[i][j])
# passing a dictionary to a function
def func1(x):
    print(x,type(x))
    for i in x:
        print(i,"=",x[i])
    return  x.setdefault('newcourse','nodejs')

# func1(a)
# returning a dictionary from function
rd=func1(a)