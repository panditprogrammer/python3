# Faulty calculator using basic operator
print("Wel come to Faulty Calculator \n")
print("Press \n")
print("1 for add")
print("2 for sum")
print("3 for multiply")
print("4 for divide")
i=int(input(" Enter here_"))

if i == 1:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    if a == 56and b == 9 :
        print("Addition is", 77)
    else:
        print("Addition is",a + b)

elif i == 2:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    print("subtraction is",a - b)

elif i == 3:
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))
    if a == 45 and b == 3 :
        print("Multiplication is", 555)
    print("multiplication is",a * b)

else:
    if i == 4:
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        if a == 56 and b == 6:
            print("division is", 4)
        print(a / b)

    else:
        print("invalid")











