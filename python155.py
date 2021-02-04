lst1=[]
for i in range(20):
    if(i%2==0):
        lst1.append(i)
print(lst1)
# this is called list comprehension video213
lst2=[ i for i in range(20 ) if i%2==0]
print(lst2)