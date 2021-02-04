# This is called set comprehension
scom={ ((i-j),(i+j)) for i in range(20,34,3) for j in range(50,60,2)}
# print(scom)

# dictionary comprehension in python
dict0={}
for i in range(10):
    dict0[i]=(10-i)

# print(dict0)
dict1={i:i+10 for i in range(0,100,12) } #this is called comprehension
print(dict1)
lit=[(10,"one"),(20,"two")]

dict7={i:j for i ,j in lit} #this is called comprehension
print(dict7)
