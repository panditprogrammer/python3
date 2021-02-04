from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.title("panditPro")
windows.minsize(300,300)


l1=Label(windows,text="Enter something",font=("Arial",16))
l1.grid(row=0,column=0,pady=20)

x=StringVar()

e1=Entry(windows,font=("Arial",16),textvariable=x)
e1.grid(row=0,column=1,pady=20)
# getting input from user and printing on console and clear input prompt
def fun1():
    s=e1.get()
    print(s)
    x.set("")

b1=Button(windows,text="Print",font=("Arial",16),command=fun1)

b1.grid(row=1,column=0,columnspan=2,pady=20)


windows.mainloop()