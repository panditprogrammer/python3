#Return statement in python single value return
#Defining a function
def add():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    c=a+b
    d=a-b
    return c, d


#calling a function
sum ,sub=add()
print( "addition is ",sum,"\n","subtraction is ",sub)

# def add():
#     a=int(input("Enter first number : "))
#     b=int(input("Enter second number : "))
#     c=a+b
#     return c
# sum=add()
# print(sum)