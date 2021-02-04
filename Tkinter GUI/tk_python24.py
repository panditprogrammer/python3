from tkinter import *
windows=Tk()
windows.geometry("480x260")
windows.title("Tic Tac Toe Game _Panditprogrammer.com")
windows.resizable(0,0)

c=1
def fun(b):
    global c
    c=c+1
    if(c%2==0):
        if(b["text"]==""):
            b["text"]="0"
            b["fg"]="green"
    else:
        if(b["text"]==""):
            b["text"]="X"
            b["fg"]="red"

"""def winner():
    if(btn1["text"]==0 and btn2["text"]==0  and btn3["text"]==0):
        print("Player First is Winner !")
    elif(btn1["text"]==X and btn2["text"]==X  and btn3["text"]==X):
        print("Player Second is Winner !")

    if (btn4["text"] == 0 and btn5["text"] == 0 and btn6["text"] == 0):
        print("Player First is Winner !")
    elif (btn4["text"] == X and btn5["text"] == X and btn6["text"] == X):
        print("Player Second is Winner !")

    if (btn7["text"] == 0 and btn8["text"] == 0 and btn9["text"] == 0):
        print("Player First is Winner !")
    elif (btn7["text"] == X and btn8["text"] == X and btn9["text"] == X):
        print("Player Second is Winner !")

    if (btn1["text"] == 0 and btn4["text"] == 0 and btn7["text"] == 0):
        print("Player First is Winner !")
    elif (btn1["text"] == X and btn4["text"] == X and btn7["text"] == X):
        print("Player Second is Winner !")

    if (btn2["text"] == 0 and btn5["text"] == 0 and btn8["text"] == 0):
        print("Player First is Winner !")
    elif (btn2["text"] == X and btn5["text"] == X and btn8["text"] == X):
        print("Player Second is Winner !")

    if (btn3["text"] == 0 and btn6["text"] == 0 and btn9["text"] == 0):
        print("Player First is Winner !")
    elif (btn3["text"] == X and btn6["text"] == X and btn9["text"] == X):
        print("Player Second is Winner !")

    if (btn3["text"] == 0 and btn5["text"] == 0 and btn7["text"] == 0):
        print("Player First is Winner !")
    elif (btn3["text"] == X and btn5["text"] == X and btn7["text"] == X):
        print("Player Second is Winner !")

    if (btn1["text"] == 0 and btn5["text"] == 0 and btn9["text"] == 0):
        print("Player First is Winner !")
    elif (btn1["text"] == X and btn5["text"] == X and btn9["text"] == X):
        print("Player Second is Winner !")"""



# changing button text using function
l1=Label(windows,fg="brown",text="first player '0' and second 'X'",font=("Arial",20))
l1.grid(row=0,column=0,columnspan=4)
btn1=Button(windows,text="",bg="white",width=8,fg="black",font=("Arial",18),command=lambda :fun(btn1))
btn1.grid(row=1,column=1)

btn2=Button(windows,text="",bg="white",fg="black",width=8,font=("Arial",18),command=lambda :fun(btn2))
btn2.grid(row=1,column=2)

btn3=Button(windows,text="",bg="white",width=8,fg="black",font=("Arial",18),command=lambda :fun(btn3))
btn3.grid(row=1,column=3)

btn4=Button(windows,text="",bg="white",fg="black",width=8,font=("Arial",18),command=lambda :fun(btn4))
btn4.grid(row=2,column=1)

btn5=Button(windows,text="",bg="white",width=8,fg="black",font=("Arial",18),command=lambda :fun(btn5))
btn5.grid(row=2,column=2)

btn6=Button(windows,text="",bg="white",fg="black",width=8,font=("Arial",18),command=lambda :fun(btn6))
btn6.grid(row=2,column=3)

btn7=Button(windows,text="",bg="white",width=8,fg="black",font=("Arial",18),command=lambda :fun(btn7))
btn7.grid(row=3,column=1)

btn8=Button(windows,text="",bg="white",fg="black",width=8,font=("Arial",18),command=lambda :fun(btn8))
btn8.grid(row=3,column=2)

btn9=Button(windows,text="",bg="white",fg="black",width=8,font=("Arial",18),command=lambda :fun(btn9))
btn9.grid(row=3,column=3)

# restart=Button(windows,text=" Restart Game ",bg="white",fg="blue",font=("Arial",18),command=lambda :fun(add_btn9))
# restart.grid(row=4,column=0,columnspan=3)

windows.mainloop()