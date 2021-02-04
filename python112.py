# def show(a):
#     print(a()*a())           # function multiply by itself
#
# show(lambda x=2:x)

# video 118
# returning lambda  function from a function

def add():
    y=int(input("Enter a number for getting double :"))
    return (lambda x:(y*2))

a=add()
print(a(1))              # 1 is for nothing use here but we can use