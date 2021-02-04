# item method for dictionary video 200
s={10:"rahul",11:"dinesh",12:"sharma"}
a=s.items()
b=list(s.items())
print(a,type(a))
print(b,type(b))
print(b[1])
print(b[2])
print(b[0])
print()
for i in b:
    for j in i:
        print(j)