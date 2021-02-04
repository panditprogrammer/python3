# try and except in python
a=(input("Enter  number"))
b=(input("Enter  number"))
try:
    print("Addition of ", a, "and ", b,"is",int(a)+int(b))

except Exception as  e:
    print(" Invalid input! Try again")
    # print(e)
print("rest of the code")
