from tkinter import *
from tkinter import ttk
windows =Tk()
windows.title("panditprogrammer")
windows.geometry("400x400")
# creating a tab for menu
n=ttk.Notebook(windows)
n.place(x=0,y=0,width=400,height=200) #height and width must be equal to geometry(

f1=Frame(bg="pink")
n.add(f1,text="menu")
b1=Button(f1,text="first page")
b1.place(x=100,y=100)

f2=Frame(bg="green")
n.add(f2,text="file")
b2=Button(f2,text="second page")
b2.place(x=100,y=100)

f3=Frame(bg="blue")
n.add(f3,text="view")
b3=Button(f3,text="third page")
b3.place(x=100,y=100)

f4=Frame(bg="red")


windows.mainloop()