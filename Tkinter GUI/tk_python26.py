from tkinter import  *
# radiobutton and entry
windows=Tk()
windows.geometry("600x400")
windows.title("radio button")
x=IntVar()
s=StringVar()

def fun_1():
    if(x.get()==1):
        s.set("Male")
    if(x.get()==2):
        s.set("FeMale")

r1=Radiobutton(windows,text="Male",variable=x,value=1,command=fun_1).pack()
r11=Radiobutton(windows,text="FeMale",variable=x,value=2,command=fun_1).pack()
e1=Entry(windows,font=("Arial",14),textvariable=s).pack()
windows.mainloop()