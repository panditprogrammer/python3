# Function in python How function work video 103
#defining a function
def demo():
    name="panditprogrammer.com"
    print("welcome to ",name)


# calling a function write once use many times
demo()
demo()
# function for adding two numbers
#defining here
def add():
    print("Enter numbers for adding:")
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    c=a+b
    print("Addition is", c)
#calling here
add()
# callign a function with arguments
print("\nfunction with arguments")
def add(a ,b):
    c=a+b
    print("Addition is",c)
add( 50 ,80)