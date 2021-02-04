# set  in python
s=set()
print(type(s))
l=[1,3,5,7,83,23]
set1=set(l)
# print(set1)
s.add(83) #to add in set
s.add(34)
s.add(34)
# print(s)
set2={34, 83,5, 7, 8}
print(s.union(set2))

print(s.intersection(set2))

print(s.difference(set2))

print(s.issubset(set2))

print(s.isdisjoint(set2))

print(max(s))
print(min(s))

set1.remove(83)
print(set1)
