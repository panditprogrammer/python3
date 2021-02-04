from tkinter import *

windows=Tk()
windows.title("Calculator_PanditProgrammer.Com")
windows.geometry("425x400")
windows.resizable(0,0)
windows.configure(bg="black")

a=StringVar()
#desplaying
try:
	def disp(c):
    a.set(a.get()+c)
except Exception as e:
	a.set(e)
else:
	pass
finally:
	pass



# def datadel(c):
#     a.set(
try:
	def solve():
    s=a.get()
    a.set(eval(s))
except Exception as e:
	a.set(e)
	print(e)
else:
	pass
finally:
	pass


# clear output

def clear():
    a.set("")

outentry=Entry(windows,font=("Arial",25),textvariable=a)
outentry.place(x=6,y=2,width=412,height=50)

b7=Button(text=7,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("7"))
b7.place(x=5,y=55,width=100,height=50)

b8=Button(text=8,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("8"))
b8.place(x=110,y=55,width=100,height=50)

b9=Button(text=9,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("9"))
b9.place(x=215,y=55,width=100,height=50)

bo1=Button(text="+",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("+"))
bo1.place(x=320,y=55,width=100,height=50)



b4=Button(text=4,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("4"))
b4.place(x=5,y=110,width=100,height=50)

b5=Button(text=5,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("5"))
b5.place(x=110,y=110,width=100,height=50)

b6=Button(text=6,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("6"))
b6.place(x=215,y=110,width=100,height=50)

bo2=Button(text="-",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("-"))
bo2.place(x=320,y=110,width=100,height=50)


b1=Button(text=1,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("1"))
b1.place(x=5,y=165,width=100,height=50)

b2=Button(text=2,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("2"))
b2.place(x=110,y=165,width=100,height=50)

b3=Button(text=3,font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("3"))
b3.place(x=215,y=165,width=100,height=50)

bo1=Button(text="*",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("*"))
bo1.place(x=320,y=165,width=100,height=50)


# bc=Button(text="C",font=("Arial",25),bg="gray",fg="white",activebackground="white")
# bc.place(x=5,y=220,width=100,height=50)

b0=Button(text="0",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("0"))
b0.place(x=5,y=220,width=205,height=50)

beq =Button(text=".",font=("Arial",25),bg="gray",fg="white",activebackground="white",command=lambda:disp("."))
beq .place(x=215,y=220,width=100,height=50)

bdiv=Button(text="/",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("/"))
bdiv.place(x=320,y=220,width=100,height=50)



# bPer=Button(text="Del",font=("Arial",25),bg="gray",fg="white",activebackground="white")
# bPer.place(x=5,y=275,width=100,height=50)

b5=Button(text="=",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=lambda:disp("="))
b5.place(x=5,y=275,width=205,height=50)
b5.configure(command=solve)

b6=Button(text="Del",font=("Arial",25),bg="gray",fg="white",activebackground="white")
b6.place(x=215,y=275,width=100,height=50)
# b6.configure(command=datadel(""))

bo2=Button(text="C",font=("Arial",30),bg="gray",fg="white",activebackground="white",command=clear)
bo2.place(x=320,y=275,width=100,height=50)


label1=Label(windows,bg="gray",fg="white",text="PanditProgrammer.Com",font=("century",20)).place(x=5,y=330,width=415,height=65)

windows.mainloop()