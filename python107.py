# Function Return another function video107
def expo():
    print("****** Square of a number ******")
    def squ():
        a = int(input("Enter a number :"))
        c=a*a
        return c
    return squ

# returning a function
b=expo()
print("Square is",b())
