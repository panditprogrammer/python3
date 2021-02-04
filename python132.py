# Yiel Statement
# Yield statement returns the elements from a generator functioon into a fuction
"""def gen1(a,b):
    yield a
    yield b

result=gen1(10,20)
print(result)
print(type(result))
l=list(result)
print(l)
print(type(l))"""
def gen(a,b):
    while a<=b:
        yield a
        a+=1

result1=gen(10,15)
print(result1)
print(type(result1))
print(next(result1))
print(next(result1))
print(next(result1))
print(next(result1))
print(next(result1))

# don't use too much next function
