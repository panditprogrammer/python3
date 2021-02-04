from  tkinter import *
windows=Tk()
windows.geometry("600x400")
windows.resizable(0,0)
windows.title("panditPro")

x=1
def fun1(e):
    global x
    x=x+1
    # x=range(1,10)
    # for i in x:
    if(x%2==0):
        windows.configure(bg="red")
    else:
         windows.configure(bg="blue")

b1=Button(windows,text="click",font=("Arial",20))
b1.bind("<Button>",fun1)
# dragging mouse on  button background will be change
b1.bind("<Motion>",fun1)
b1.pack()





windows.mainloop()