#Higher order function in python
# reduce function in python
from functools import *

# importing for reduce( )

a=[11,22,33,44,55,66,77,88,99,100]

result=reduce(lambda n,m:n+m,a)

print(result)
print(type(result))