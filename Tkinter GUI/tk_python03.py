#Entry in windows input field
from tkinter import *
#creating a object name root of Tk
root=Tk()


root.geometry("400x400")
root.resizable(0,0)
# creating a label and input prompt using Label() and Entry()
user_name_label=Label(root,text="Enter Your Name",font=("Arial ",16),fg="blue",bg="red").pack()
user_name =Entry(root,font=("Arial ",16),fg="blue",bg="red").pack()




root.mainloop()