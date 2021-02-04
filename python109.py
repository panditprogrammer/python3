#Variable lenth Arguments in python
def add(*numb):  #     " * " is a vaiable lenth
    a=numb[0]+numb[1]
    print("Addition is")
    return a

#calling here
b=add(20,10,8)
print(b)