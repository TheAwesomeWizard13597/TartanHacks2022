
from logging import root
from re import L
import tkinter
from tkinter import *
from data import *

def show_places():
    for i in range(10):
        #place = risk['Country']
        #rLevel = risk['Active']
        
        if(rLevel > w.get()):
            continue
        pltext = str(i+1) + ". " + place + '! You can travel here since the risk level is only +' str(rLevel)
        llist[i].config(text=pltext)
        llist[i].pack()

# Initialize root and place list
root = Tk()
llist = [Label(root), Label(root), Label(root), Label(root), Label(root), Label(root), Label(root), Label(root), Label(root), Label(root)]

# Add Title text and instructions
l1 = Label(root, text = "Covid Risk-Assessment Tool")
l1.config(font =("Arial", 16))
l2 = Label(root, text = "This tool is designed to show you where you \
should travel based on your risk-comfort level. Use the slider to \
select your preference and then click the \"Refresh\" button to see \
potential travel locations.",wraplengt=400)
l1.pack()
l2.pack()

# Add scaler and refresh button
w = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=500)
w.pack()
Button(root, text='Refresh', command=show_places).pack()

# Adding canvas may not be necessary
# canvas = tkinter.Canvas(root, height=400, width=600)
# canvas.configure(bd=0, highlightthickness=0)
# canvas.pack()

root.mainloop()