from tkinter import *

windows=Tk()
windows.geometry("600x400")
windows.title("Press 1,2,3,4,5,6,7 to change background color")

windows.bind("1",lambda e:windows.configure(bg="red"))
windows.bind("2",lambda e:windows.configure(bg="green"))
windows.bind("3",lambda e:windows.configure(bg="blue"))
windows.bind("4",lambda e:windows.configure(bg="white"))
windows.bind("5",lambda e:windows.configure(bg="black"))
windows.bind("6",lambda e:windows.configure(bg="orange"))
windows.bind("7",lambda e:windows.configure(bg="tomato"))
windows.bind("8",lambda e:windows.configure(bg="violet"))
windows.bind("9",lambda e:windows.configure(bg="pink"))
windows.bind("0",lambda e:windows.configure(bg="yellow"))




windows.mainloop()