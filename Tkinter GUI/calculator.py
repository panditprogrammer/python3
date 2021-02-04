from tkinter import *
windows =Tk()

windows.geometry("400x500")
windows.title("Calculator-PanditProgrammer.com")
windows.wm_iconbitmap("cal.ico")
# this is for getting number from button
def click(event):
    global  scvalue
    text= event.widget.cget("text")
    print(text)
    if text == "C":
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(windows, textvar=scvalue,font="lucida 20 bold")
screen.pack(fill=X, ipadx=8, pady=10,padx=10)

f= Frame(windows, bg="gray")

b = Button(f,text="9",font="lucida 30 bold" padx=20,pady=20,)
b.pack()

b = Button(f,text="8",font="lucida 30 bold" padx=20,pady=20,)
b.pack()

b = Button(f,text="7",font="lucida 30 bold" padx=20,pady=20,)
b.pack()
f.pack()

windows.mainloop()