from tkinter import *

windows=Tk()
windows.geometry("600x400")
# creating a button and getting function invoke
def fun1():
    print("Button function is working..")
    windows.configure(bg="gray")

b1=Button(windows,text="click me",font=("Arial",20))
b1.grid(row=0,column=0)
b1.config(command=fun1)# command for  b1

windows.mainloop()