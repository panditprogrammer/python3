# creating a button using Button()

from  tkinter import *
# creating a windows using Tk()  classmethod

windows=Tk()
windows.geometry("400x400")

button_one=Button(windows,text="click me",font=("Arial",14))
button_one.pack()



windows.mainloop()
