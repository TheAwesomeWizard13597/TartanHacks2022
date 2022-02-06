
from logging import root
import tkinter
from tkinter import *

def show_values():
    print (w.get())

# Initialize root
root = Tk()

# Add scaler and refresh button
w = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=500)
w.pack()
Button(root, text='Refresh', command=show_values).pack()

# Add canvas
canvas = tkinter.Canvas(root, height=400, width=600)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()

root.mainloop()