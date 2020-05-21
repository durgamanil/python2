# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:38:52 2019

@author: Onyx1
"""
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk


#path = 'C:/xxxx/xxxx.jpg'
path = 'F:\my_workspace\python_workspace\onyx-logo.png'


root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()