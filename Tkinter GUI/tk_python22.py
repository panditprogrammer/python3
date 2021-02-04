from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.title("panditprogrammer.com")

# getting input from user and
# printing table of a number in console
x=IntVar()
def fun():
    a=x.get()
    for i in range(1,11):
        print(i*a)
entry1=Entry(windows,font=("Arial",16),fg="green",textvariable=x)
entry1.grid(row=0,column=0)

add_btn=Button(windows,text=" click ",bg="white",fg="black",font=("Arial",16),command=lambda :fun())
add_btn.grid(row=1,column=0)

windows.mainloop()