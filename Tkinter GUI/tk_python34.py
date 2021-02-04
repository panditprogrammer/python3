from tkinter import *
windows= Tk()
windows.geometry("600x400")
windows.title("login form")
def login():
    f1 = Frame()
    f1.place(x=0,y=0,width=600,height=400)
    namelable=Label(f1,text="Enter Your Name :",font=("Arial",18)).pack()
    nameentryl=Entry(f1,font=("Arial",16)).pack()
    passlable=Label(f1,text="Enter Your password :",font=("Arial",18)).pack()

    passentryl=Entry(f1,font=("Arial",16)).pack()
    logbtn=Button(f1,text="Log In",font=("Arial",18)).pack()
    logbtn=Button(f1,text=" Back",font=("Arial",18),command=home).pack()


def resister():
    f2 = Frame()
    f2.place(x=0,y=0,width=600,height=400)

    namelable=Label(f2,text="Enter Your Name :",font=("Arial",18)).pack()
    nameentryr=Entry(f2,font=("Arial",16)).pack()

    emaillable=Label(f2,text="Enter Your Email :",font=("Arial",18)).pack()
    emailentryr=Entry(f2,font=("Arial",16)).pack()

    passlable=Label(f2,text="Enter Your Password :",font=("Arial",18)).pack()
    passentryr=Entry(f2,font=("Arial",16)).pack()

    resistbtn=Button(f2,text="Resister",font=("Arial",18)).pack()
    backbtnr=Button(f2,text=" Back",font=("Arial",18),command=home).pack()

def home():
    fmain=Frame()
    fmain.place(x=0,y=0,width=600,height=400)
    logbtn=Button(fmain,text="Log In",font=("Arial",18),command=login)
    logbtn.pack()
    resistbtn=Button(fmain,text="Resister",font=("Arial",18),command=resister)
    resistbtn.pack()



home()

windows.mainloop()
