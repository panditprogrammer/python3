# all about list
"""a=[71,72,73,74,75,76,77,78,79,80]
b=[61,62,63,64,65,66,67,68,69,70]
c=a+b
print(a)
print(b)
print("after concatenate of list")
print(c)"""
d=[61,62,63,64,65,66,67,68,69]
e=d * 2       # asterisk is used for reapeting  same thing
print("asterisk is called reapetion operator in python")
print(e)

print(" after aliasing ")
f=d     # Aliasing list means giving another name
f[4]=100
print(f)
print(d)
for i in f:
    print(i)
