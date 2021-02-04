#Dictionary         A dictionary represent a group of elements in the form of key value pairs.
student={1:"suraj",2:"prity",3:"rahul",4:"shruti"}
print(student,type(student))
print(student[2])
# modifying dictionary
# we can modify th existing value of key by asinging a new value
student[1]="anjali"
print(student[1])
# adding/ inserting new item in dictionary
student[5]="navin"
print(student[5])
print(student)
#deleting an item in dictionary and iEntire  dictionary
# del student
# how to test dictionary key existing or not
t= 2 in student
t1= 7 in student
t2= 5 in student
print(t1)
print(t2)
print(t)
student.clear()
print("after clearing ",student)

