# String in python  and memory Allocation
str1= "This is string in python"
print(str1)
"""yes , we can write like this 
  anything here  and it is used as a string usin variable"""
str2=('''This is multiline comments in python
we are writing comments in python''')
print(str2)
# double quotes in single quotes
print("This is 'notepad '")
print('This is "notepad"')
#memory allocation in python
str4= "chandan"
str5="pandit"
str6="pandit"
str7=str4
print("str4",id(str4))
print("str6",id(str6))
print("str5",id(str5))
print("str7",id(str7))
print("after changing str5")
str5="kumar"
print("str5 now ",id(str5))
print(str5)
