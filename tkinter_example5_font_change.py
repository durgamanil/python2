# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:07:42 2019

@author: Onyx1
"""

from tkinter import *
from pprint import pprint

scr = Tk()
scr.title("Label - Tkinter Widgets")

lbl = Label(scr, text="Hello", padx=5, pady=10, font=("Bold Script", 20))
lbl1 = Label(scr, text="Hello", padx=10, pady=10, font=("Bold Fraktur", 20))
lbl2 = Label(scr, text="Hello", padx=15, pady=10, font=("Arial Bold", 20))


lbl.pack()
pprint(dict(lbl))
pprint(dict(lbl1))
pprint(dict(lbl2))
scr.mainloop()