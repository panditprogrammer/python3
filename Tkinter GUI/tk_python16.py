from tkinter import *
windows= Tk()
windows.geometry("600x400")
windows.title("PanditPro")
# getting input from user and printing on console
def fun1():
    s=e1.get()
    print("You have typed",'"',s,'"')

l1=Label(windows,text="Enter something",font=("Arial",16),pady=20)
l1.grid(row=0,column=0,sticky="w")

e1=Entry(windows,font=("Arial",16))
e1.grid(row=0,column=1,sticky="e")
b1=Button(windows,text="print on console",font=("Arial",16),command=fun1)
b1.grid(row=1,column=0,columnspan=2,sticky="n")




windows.mainloop()