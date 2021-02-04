from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.resizable(0,0)
windows.title("Simple calculator_PanditProgrammer.com")
x=DoubleVar()
y=DoubleVar()
z=DoubleVar()

def fun(o):
    a=x.get()
    b=y.get()
    if(o==1):
        c=a+b
        z.set(c)
    elif(o==2):
        c = a - b
        z.set(c)
    elif(o==4):
        c = a * b
        z.set(c)
    elif(o==3):
        c = a / b
        z.set(c)

top_label=Label(windows,text="Simple calculator for ( +, -, *, / ) ",font=("Arial",18),fg="brown")
top_label.grid(row=0,column=0,columnspan=2,sticky="e")

label_input1=Label(windows,text="Enter first number ",font=("Arial",16),fg="black",pady=25)
label_input1.grid(row=1,column=0,sticky="w")
label_input2=Label(windows,text="Enter second number ",font=("Arial",16),fg="black",)
label_input2.grid(row=2,column=0,sticky="w")

entry1=Entry(windows,font=("Arial",16),fg="green")
entry1.grid(row=1,column=1)
entry2=Entry(windows,font=("Arial",16),fg="green",textvariable=y)
entry2.grid(row=2,column=1)

add_btn=Button(windows,text=" Add (+) ",bg="white",fg="black",font=("Arial",16),command=lambda :fun(1))
add_btn.grid(row=3,column=0,columnspan=4)

sub_btn=Button(windows,text=" Sub (-) ",bg="white",fg="black",font=("Arial",16),command=lambda :fun(2))
sub_btn.grid(row=3,column=0)

div_btn=Button(windows,text=" Div (/) ",bg="white",fg="black",font=("Arial",16),command=lambda :fun(3))
div_btn.grid(row=4,column=0)

multi_btn=Button(windows,text=" Multi (*) ",bg="white",fg="black",font=("Arial",16),command=lambda :fun(4))
multi_btn.grid(row=4,column=0,columnspan=2)

resullabel=Label(windows,text="Result ",font=("Arial",16),fg="black",pady=20)
resullabel.grid(row=5,column=0,sticky="e")

result=Entry(windows,font=("Arial",17),fg="green",textvariable=z)
result.grid(row=5,column=1)

windows.mainloop()