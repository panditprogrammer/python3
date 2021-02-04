# join ,replace and split function in python
# This is replace function
n='This is panditprogrammer.'
old="panditprogrammer"
new="python file"
a=n.replace(old,new)
print(n)
print("after removing 'panditprogrammer'..")
print(a)

#This is split function
print("\nbefore spliting...")
b="Hi I am programmer."
print(b)
d=b.split(" ")
print("after spliting ... we got")
print(d)
# This is join function
print("\nbefore joining ")
x=('this','is', 'python','file')
print(x)
y= " ".join(x)
print("after joining..")
print(y)