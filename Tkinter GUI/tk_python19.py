from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.title("Addition of two numbers _panditprogrammer.com")
windows.minsize(300,300)
a=DoubleVar()      
b=DoubleVar()
c=DoubleVar()
def add():
    a1=(a.get())
    b1=(b.get())
    c1=a1+b1
    c.set(c1)

label_1=Label(windows,text="Enter first number",font=("Arial",16))
label_1.grid(row=0,column=0,pady=15)

label_2=Label(windows,text="Enter second number",font=("Arial",16))
label_2.grid(row=1,column=0,pady=15)

Entry_a=Entry(windows,font=("Arial",16),fg="green",textvariable=a)
Entry_a.grid(row=0,column=1)

Entry_b=Entry(windows,font=("Arial",16),fg="green",textvariable=b)
Entry_b.grid(row=1,column=1)
add_btn=Button(windows,text="Add",font=("Arial",16),command=add)
add_btn.grid(row=2,column=0,columnspan=2)

Entry_c=Entry(windows,font=("Arial",16),fg="blue",textvariable=c)
Entry_c.grid(row=3,column=0,columnspan=2)


windows.mainloop()