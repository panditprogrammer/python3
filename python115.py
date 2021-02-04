# Function Decorator video 126
# A Decorator function is a function that accept a function as parameter and returns a function.
# A decorator takes the result of a function, modifies the result and returns it.
"""def fill1(x):
    print("This is function")
    def fill2():
        x()
        print("This is second function")
    return fill2()

def fun1():
    print("This is function which is used for decorator")

a=fill1(fun1)
print(a)"""