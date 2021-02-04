from tkinter import *
windows= Tk()
windows.geometry("600x400")
windows.title("PanditProgrammer")
# for windows background changing on pressing button

windows.bind("<Key-a>",lambda e: windows.configure(bg="white"))
windows.bind("<Key-b>",lambda e: windows.configure(bg="green"))
windows.bind("<Key-c>",lambda e: windows.configure(bg="blue"))
windows.bind("<Key-d>",lambda e: windows.configure(bg="pink"))
windows.bind("<Key-f>",lambda e: windows.configure(bg="yellow"))
windows.bind("<Key-e>",lambda e: windows.configure(bg="red"))

l1=Label(windows,font=("Arial",14),text="Press a,b,c,d,e,f to change background color")
l1.grid(row=0,column=1)

b1=Button(windows,text="click me",font=("Arial",14))
# mouse movement on b1
b1.bind("<Enter>",lambda e:windows.configure(bg="orange"))
b1.bind("<Leave>",lambda e:windows.configure(bg="black"))

b1.grid(row=0,column=0,)


windows.mainloop()