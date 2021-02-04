from tkinter import  *
# spinbox and
windows=Tk()
windows.title("panditprogrammer")
windows.geometry("400x400")
a=StringVar()

def colo():
    windows.configure(background=a.get())

s1=Spinbox(font=("Arial",20),command=colo,textvariable=a,value=["red","green","blue","pink","orange"])
s1.pack()


# b1=Button(text="click",font=("Arial",20),command=colo)
# b1.pack()

windows.mainloop()