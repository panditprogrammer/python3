from tkinter import *

# creating a basic form
windows=Tk()
windows.geometry("400x400")

name=Label(windows,text="Enter username",font=("Arial",14)).grid(row=0,column=0,pady="20",padx="20",sticky="w")
name_entry=Entry(windows,font=("Arial",18)).grid(row=0,column=1)

password=Label(windows,text="Enter Password",font=("Arial",14)).grid(row=1,column=0,sticky="w",padx="20")
# show="you can put any symbol"
pass_entry=Entry(windows,show="*",font=("Arial",18)).grid(row=1,column=1)
# margin column and row using columnspan and rowspan
submit_button=Button(windows,text="Login",font=("Arial",18)).grid(row=2,column=0,columnspan="2",pady="22")



windows.mainloop()