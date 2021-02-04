# passing a array in a function
from array import *
"""def a(x):
    print("This is a function")
    print(x)
    print(type(x))
    print("array using for loop")
    for i in x:
        print(i)

arr=array('i',[101,102,103,104,105,106,107,108])

# calling function here
a(arr)"""

# passing and returning a array from function in python

def funar(x):
    print(x)
    a=array('i',[11,12,13,14,15,16,17,18,19,20])
    print(a)
    return a

str= "Hi ,\n This is array"
r=funar(str)
print(type(r))