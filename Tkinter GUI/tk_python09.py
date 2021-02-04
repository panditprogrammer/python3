from tkinter import *

windows=Tk()
windows.title("PanditProgrammer.com")

windows.geometry("600x400")

fun1 =lambda e:windows.configure(bg="pink")
fun2 =lambda e:windows.configure(bg="red")
fun3 =lambda e:windows.configure(bg="green")
l1=Label(windows,text="Double click button to see effects on background",font=("Arial",17))
l1.grid(row=0,column=0)
b1=Button(windows,text="click me",font=("Arial",17))
b1.bind("<Double-1>",fun1)
b1.bind("<Double-2>",fun2)
b1.bind("<Double-3>",fun3)
b1.grid(row=1,column=0)


windows.mainloop()