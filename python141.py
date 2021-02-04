# set Type in python
# A set does'nt accept duplicated elements
# A set is unorder collection of elements
a={10,20,30,40,50,60,740,50,60,70,80,90}
print(a,type(a))
# we can crate an empty set using set( function.
s=set()
print(s)
s.update((20,30,"pandit",00,"nothing"))
print(s ,id(a))
print(id(a))
# we can add new element in set using add method
a.add("python")
print(a,id(a))
# we can add multiplevalue using updte method
a.update(["CHANDAN","chandan","pandit","panditprogrammer"])
print(a,id(a))