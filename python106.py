#passing a function as a parameter
#We can pass a function as  a parameter to another nuction
def function1(f1):
    print("what is your Name?")
    b=f1()
    return b

    #Here is second function
def function2():
    a=input("Enter here :")
    return a

#Calling function
z=function1(function2) # passing a function
print("Your Name is",z)

    