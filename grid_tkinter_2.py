# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:41:56 2020

@author: Onyx1
"""

import tkinter as tk

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
    tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
    r = r + 1

tk.mainloop()