from tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.title("panditprogrammer.com")


def fun(b):
    b["text"]="submit"
    b["fg"]="black"
    b["bg"]="white"
    b["width"]=20
    b["height"]=3


# changing button text using function size and more

add_btn=Button(windows,text=" click ",bg="white",fg="black",font=("Arial",16),command=lambda :fun(add_btn))
add_btn.grid(row=1,column=0)

windows.mainloop()