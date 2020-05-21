# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:57:53 2019

@author: Onyx1
"""

from Tkinter import *

rows = []
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print(col.get())
Button(text='Fetch', command=onPress).grid()
mainloop()