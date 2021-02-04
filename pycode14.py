a=int(input("Enter  number"))
b=int(input("Enter  number"))
# c= sum((a,b))
# print(c)

def addi(a,b):
    """This is function for calculating average of two number"""
    print(" This is function")
    v=(a+b)/2
    print("average",v)
    # return v

s=addi(a,b)
print(addi.__doc__) # This is called doc string for getting comment about function