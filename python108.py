#Keyword arguments in python video 110
def name1(fname, lname="Pandit"):
    print(fname,lname)
    #This function is not return anything
name1("Chandan","Pandit")
name1(fname="Pandit",lname="Programmer")
# calling once again here
name1(lname="Programmer",fname="Pandit")

name1("Chandan")# here second argument is not passing