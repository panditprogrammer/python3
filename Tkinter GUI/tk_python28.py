from tkinter import *

# spinbox and
windows = Tk()
windows.title("panditprogrammer")
windows.geometry("400x400")
a = StringVar()


def numb():
    print(a.get())

# getting number from spinbox and printing on console
s1 = Spinbox(font=("Arial", 20), command=numb, textvariable=a,from_=5,to=15)
s1.pack()



windows.mainloop()