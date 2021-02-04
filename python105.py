#Nested Function in python
#Multiplication of two numbers
def m():
    print("Multiplication of two numbers :: -")
    #here starts second function of nested function
    def multi():
        a=int(input("Enter a number : "))
        b=int(input("Enter another number : "))
        c=a*b
        return c
    d=multi()
    return d
#calling main function of nested function

e=m()
print(e)


