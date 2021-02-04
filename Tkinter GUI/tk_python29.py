from tkinter import *
windows =Tk()
windows.title("panditprogrammer")
windows.geometry("400x400")
# creating a checkbox
a=IntVar()
b=IntVar()
s=StringVar()
def fun1():
    s1=""
    if(a.get()==1):
        s1+="python"
    if(b.get()==1):
        s1+="c/c++"
    s.set(s1)

c1=Checkbutton(windows,text="python",font=("Arial",18),variable=a).pack()
c11=Checkbutton(windows,text="c/c++",font=("Arial",18),variable=b).pack()

b1=Button(windows,text="click",font=("Arial",18),command=fun1).pack()

e1=Entry(windows,font=("Arial",18),textvariable=s).pack()

windows.mainloop()