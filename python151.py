# setdefault method in python
s={12:"first",11:"second",10:"third"}
print(s)
result=s.setdefault(11,'forth')
print(s)
print(result)
# result=s.setdefault(19,'forth')
# print(s)
# print(result)
# accessing dictionary using for loop
diction1={10:"rahul",11:"dinesh",12:"sharma"}
for i in diction1:
    print(i,diction1[i])

# getting input from user in dictionary
dict1={}
n=int(input("Enter times"))
for i in range(n):
    k=input("Enter keys")
    v=input("Enter values")
    dict1.update({k: v})
print(dict1)