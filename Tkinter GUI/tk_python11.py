from tkinter import  *

windows = Tk()
windows.geometry("600x400")
windows.resizable(0,0)
windows.title("PanditPro")

windows.bind("<F1>",lambda e:windows.configure(bg="red"))
windows.bind("<r>",lambda e:windows.configure(bg="red"))
windows.bind("<F2>",lambda e:windows.configure(bg="green"))
windows.bind("<g>",lambda e:windows.configure(bg="green"))
windows.bind("<F3>",lambda e:windows.configure(bg="blue"))
windows.bind("<b>",lambda e:windows.configure(bg="blue"))
windows.bind("<F4>",lambda e:windows.configure(bg="white"))
windows.bind("<w>",lambda e:windows.configure(bg="white"))
windows.bind("<F5>",lambda e:windows.configure(bg="black"))
windows.bind("<F6>",lambda e:windows.configure(bg="violet"))
windows.bind("<v>",lambda e:windows.configure(bg="violet"))
windows.bind("<F7>",lambda e:windows.configure(bg="orange"))
windows.bind("<o>",lambda e:windows.configure(bg="orange"))
windows.bind("<F8>",lambda e:windows.configure(bg="tomato"))
windows.bind("<t>",lambda e:windows.configure(bg="tomato"))



windows.mainloop()