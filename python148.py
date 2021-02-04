# Creating a dictionary using formkeys method
a=(12,83,87,)
b=(12,7,38)
diction=dict.fromkeys(a,b)
# it will create  like this   {12: (12, 7, 38), 83: (12, 7, 38), 87: (12, 7, 38)}
print(diction)

# get method in python
# This method returns the value of the specified key. if it not found retun nne
s={10:"rahul",11:"dinesh",12:"sharma"}
sr=s.get(10) # it will return value of key
print(sr)