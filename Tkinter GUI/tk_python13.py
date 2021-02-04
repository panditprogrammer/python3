from tkinter import *

windows=Tk()
windows.geometry("600x400")
windows.title("Press Ctrl+Up down left right ,Shift+Up down left right ,Alt+Up, Alt-down to change background color")

windows.bind("<Shift-Up>",lambda e:windows.configure(bg="red"))
windows.bind("<Shift-Down>",lambda e:windows.configure(bg="green"))
windows.bind("<Shift-Left>",lambda e:windows.configure(bg="blue"))
windows.bind("<Shift-Right>",lambda e:windows.configure(bg="white"))
windows.bind("<Alt-Up>",lambda e:windows.configure(bg="black"))
windows.bind("<Alt-Down>",lambda e:windows.configure(bg="orange"))
windows.bind("<Alt-Left>",lambda e:windows.configure(bg="tomato"))
windows.bind("<Alt-Right>",lambda e:windows.configure(bg="violet"))
windows.bind("<Control-Up>",lambda e:windows.configure(bg="pink"))
windows.bind("<Control-Down>",lambda e:windows.configure(bg="yellow"))

def b1_fun(e):
    windows.configure(bg="black")
b1=Button(windows,text="click",font=("Arial",20))
b1.bind("<Button>",lambda e:windows.configure(bg="red"))
# after release button background will be change
b1.bind("<ButtonRelease>",b1_fun)
b1.pack()




windows.mainloop()