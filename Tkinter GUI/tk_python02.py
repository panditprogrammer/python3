from tkinter import  *
# this is the second video on tkinter
root=Tk()
root.geometry("400x500")
root.resizable(0,0)

firstname=Label(root,text="First name",
                width="10" ,bg="gray",height="1",fg="white",font=("Arial" ,20)).grid()
lastname=Label(root,text="Last name",fg="white",
               width="10" ,bg="gray",height="1",font=("Arial" ,20)).grid()
root.mainloop()