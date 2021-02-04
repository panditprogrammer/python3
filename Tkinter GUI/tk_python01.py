from tkinter import *
#creating a windows

root=Tk()
# geometry is used to create windows size
root.geometry("600x400")


# To creating a label or text you must use Label class
labelg=Label(root,text="This is windows",fg= "red", font=("Arial",20))
# fg for forground color and bg for background color to change font color

lab1=Label(root,fg="blue",text="this is another\n label",font=("Arial",20)).pack()
# .pack is used for packing on windows and displaying
labelg.pack()
lab2=Label(root,bg="gray",width="20",height="3",text="label 2"  ,
           fg="green",font=("Arial",18)).pack()
#minsize is used for windows size
root.minsize(480,300)
text=Label(text="This is simple windows.",font=("Arial 16")).pack()

root.mainloop()

print(" after mainloop run successfully")


