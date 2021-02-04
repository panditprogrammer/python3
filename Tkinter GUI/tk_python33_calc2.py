from tkinter import *
windows=Tk()
windows.title("Calculator_PanditProgrammer.Com")
windows.geometry("425x420")
windows.resizable(0,0)
windows.configure(bg="black")
a=StringVar()
#desplaying
def disp(c):
        # a.set("    Error...   ")
        a.set(a.get() + c)
def solve():
    s=a.get()
    # if (s!= "none"):
    a.set(eval(s))
        # print(a.set(eval(s)))
    # else:
    #     a.set("  Error...  ")
# clear output
def clear():
    a.set("")
outentry=Entry(windows,font="lucida 28 bold",textvariable=a)
outentry.place(x=6,y=5,width=412,height=55)
b=[Button()]*16
data=["7","8","9","+","4","5","6","-","1","2","3","*","C","0",".","/"]
x=5
y=70
B=0
for i in range(4):
    for j in range(4):
        b[B]=Button(text=data[B],font="lucida 25 bold",bg="gray",fg="white")
        b[B].place(x=x,y=y,width=100,height=50)
        B+=1
        x+=105
    x=5
    y+=55
b[0].configure(command=lambda :disp(data[0]))
b[1].configure(command=lambda :disp(data[1]))
b[2].configure(command=lambda :disp(data[2]))
b[3].configure(command=lambda :disp(data[3]))
b[4].configure(command=lambda :disp(data[4]))
b[5].configure(command=lambda :disp(data[5]))
b[6].configure(command=lambda :disp(data[6]))
b[7].configure(command=lambda :disp(data[7]))
b[8].configure(command=lambda :disp(data[8]))
b[9].configure(command=lambda :disp(data[9]))
b[10].configure(command=lambda :disp(data[10]))
b[11].configure(command=lambda :disp(data[11]))
b[12].configure(command=clear)
b[13].configure(command=lambda :disp(data[13]))
b[14].configure(command=lambda :disp("."))
b[15].configure(command=lambda :disp(data[15]))
beq=Button(text="=",font=("Arial",25),bg="gray",fg="white",activebackground="white",command=solve)
beq.place(x=5,y=290,width=415,height=50)
label1=Label(windows,bg="gray",fg="white",text="PanditProgrammer.Com",font=("century",20)).place(x=5,y=345,width=415,height=65)
windows.mainloop()