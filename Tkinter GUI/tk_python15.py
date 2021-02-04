from tkinter import *

windows=Tk()
windows.title("panditPro")
windows.geometry("600x400")

e1=Entry(windows,font=("Arial",20))  #grid(row=0,column=1)
e2=Entry(windows,font=("Arial",20))         #grid(row=0,column=1)
#l1=Label(windows,text="Enter here",font=("Arial",20)).grid(row=0,column=0)
# FocusIn and focusOut
e1.bind("<FocusIn>",lambda e:windows.configure(bg="pink"))
e1.bind("<FocusOut>",lambda e:windows.configure(bg="yellow"))
e1.pack()
e2.pack()

windows.mainloop()