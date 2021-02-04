#keyword variable lenth arguments
def add(x,**num):
    a = x+ num['e'] + num['f']+(x+5)
    print("addition is")
    return a


#calling with keyword variable lenth arguments
A=add(10, e=12, f=78,g=45)  # no  require maintaining keyword arguaments
print(A)

