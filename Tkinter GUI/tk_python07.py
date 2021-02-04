from tkinter import *

windows=Tk()
windows.geometry("600x400")
# creating a button and getting function invoke
def fun1(e):
    print("Button function is working..")
    windows.configure(bg="pink")
def fun2(e):
    print("Button function is working..")
    windows.configure(bg="red")
def fun3(e):
    print("Button function is working..")
    windows.configure(bg="blue")

b1=Button(windows,text="click me",font=("Arial",20))
b1.grid(row=0,column=0)

# mouse event on clicking button
b1.bind("<Button-1>",fun1)  #this is for left means button-1
b1.bind("<Button-2>",fun2)      #this is for wheel means button-2
b1.bind("<Button-3>",fun3)      #this is for right means button-3
windows.mainloop()