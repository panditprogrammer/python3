from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.title("Radio Button")

x=IntVar()
r1=Radiobutton(windows,text="Male",variable=x,value=1).pack()
r2=Radiobutton(windows,text="FeMale",variable=x,value=2).pack()
windows.mainloop()
