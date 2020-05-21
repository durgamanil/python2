# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:40:00 2019

@author: Onyx1
"""

from tkinter import * 

def notdone():  
    showerror('Not implemented', 'Not yet available') 
     
def makemenu(parent):
    menubar = Frame(parent)                        
    menubar.pack(side=TOP, fill=X)
    
    fbutton = Menubutton(menubar, text='File', underline=0)
    fbutton.pack(side=LEFT)
    file = Menu(fbutton)
    file.add_command(label='New...',  command=notdone,     underline=0)
    file.add_command(label='Open...', command=notdone,     underline=0)
    file.add_command(label='Quit',    command=parent.quit, underline=0)
    fbutton.config(menu=file)
     
    ebutton = Menubutton(menubar, text='Edit', underline=0)
    ebutton.pack(side=LEFT)
    edit = Menu(ebutton, tearoff=0)
    edit.add_command(label='Cut',     command=notdone,     underline=0)
    edit.add_command(label='Paste',   command=notdone,     underline=0)
    edit.add_separator()
    ebutton.config(menu=edit)
     
    submenu = Menu(edit, tearoff=0)
    submenu.add_command(label='Spam', command=parent.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone,     underline=0)
    edit.add_cascade(label='Stuff',   menu=submenu,        underline=0)
    return menubar
     
root = Tk()
#for i in range(3):
frm = Frame()  
mnu = makemenu(frm)
mnu.config(bd=2, relief=RAISED)
frm.pack(expand=YES, fill=BOTH)
Label(frm, bg='black', height=5, width=15).pack(expand=YES, fill=BOTH)
Button(root, text="Bye", command=root.quit).pack()
root.mainloop()








