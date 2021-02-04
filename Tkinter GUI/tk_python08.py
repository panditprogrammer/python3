from tkinter import *

windows=Tk()
windows.geometry("600x400")
windows.title("panditprogrammer")

fun1 = lambda e:windows.configure(bg="pink")
fun2=lambda e:windows.configure(bg="blue")
fun3=lambda e:windows.configure(bg="green")

b1=Button(windows,text="click",font=("Arial",16))
# this is for binding with mouse button
b1.bind("<Button-1>",fun1)
b1.bind("<Button-2>",fun2)
b1.bind("<Button-3>",fun3)
# after binding then pack b1
b1.pack()
windows.mainloop()