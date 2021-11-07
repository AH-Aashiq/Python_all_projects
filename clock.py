from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("clock")

def time():
     string = strftime('%H:%M:%S %p')
     label.config(text = string)
     label.after(1000, time)

label = Label(root, font = ("ds-digital",100), background = "black", foreground = "cyan")
label.grid(row = 5 , column = 0)
label.pack(anchor = "center")

time()
mainloop()
