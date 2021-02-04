#Immediately Invoked Function Expressions (IIFE)
# (lambda x:print(x+10))(5)
# small and effective  (5) is for giving argument
# video 120 local variable in python
"""def fun1():
    x=int(input("Enter a number for getting square "))
    print("Square is ",x*x)

fun1()         # x is local variable because is it under function fun1
print(x)   #here i'm trying to access x but it is not possible
"""
# Global variable is declare above a function,it become a global variable.
"""a=12  #These are global variable we can access anywhere in program
b=30
def function1():
    x=int(input("Enter a number : "))   #this is local variable 
    print(x)
    print(a,b)   # here we can access global variable a,b

function1()"""

# video 122 global keyword
#  If local variable and global variable has same name then the function by default refers to the local variable an dignores the gloabal variable
"""a=20
i=0     # this is changing from function
def show():
    global i  # here is global keyword for identify this  is global variable
    print("Total number is ")
    while i<10:
        print(i)
        i+=1
        if i==10:
            break
show()

print("this is from outside of function ",i)"""

#  video 123 This function returns a table of current global variable  in the form of dictionary

a=20
def fun2():
    a=10
    print(a)
    b=globals()['a']   # here is global function  for accessing
    # 'a' in the form of 'b' it is returns dictionay
    print(b)

fun2()