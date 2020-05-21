# -*- coding: utf-8 -*-
"""
Created on :27-12-2019
@author: anil durgam
version:1.2
example:MM32 microcontroller drop down menu
"""

#****************************library import sections****************
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3
from PIL import ImageTk, Image
from pprint import pprint
scr = Tk()
#path = 'F:\my_workspace\python_workspace\onyx-logo1.jpg'

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Micro controller Selector")
        tk.Label(main_window,text="MM32 microcontroller selected",fg = "blue",font = "Times").pack()
        
        self.combo = ttk.Combobox(self)
        self.combo.place(x=50, y=120)
        self.combo["values"] = ["MM32F", "MM32L",  "MM32W", "MM32SPIN", "MM32P"]
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        main_window.configure(width=1024, height=500)
        self.place(width=300, height=300)
        
    def selection_changed(self, event):
        print("your selected::", self.combo.get())
        if self.combo.get()== "MM32F" :
            #print("mm32f submenu displayed here\n")
            T.insert(tk.END, "MM32F Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
            

        elif self.combo.get()== "MM32L" :
            #print("mm32L submenu displayed here\n")
            T.insert(tk.END, "MM32L Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            self.combo["values"] = ["MM32L050", "MM32L051", "MM32L052", "MM32L061",
                      "MM32L062","MM32L072","MM32L073","MM32L362","MM32L373","MM32L384",
                      "MM32L395"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
                
        elif self.combo.get()== "MM32W" :
            #print("mm32W submenu displayed here\n")
            T.insert(tk.END, "MM32W Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            self.combo["values"] = ["MM32W051", "MM32W062", "MM32W073", "MM32W362"
                      , "MM32W373", "MM32W384", "MM32W395"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
                    
        elif self.combo.get()== "MM32SPIN" :
            #print("mm32SPIN submenu displayed here\n")
            T.insert(tk.END, "MM32SPIN Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
            
        else :
            #print("mm32P submenu displayed here\n")
            T.insert(tk.END, "MM32P Family is selected\n")
            self.combo = ttk.Combobox(self)
            self.combo.place(x=50, y=160)
            self.combo["values"] = ["MM32F003", "MM32F031", "MM32F032", "MM32F103"]
            self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
            
#=========================main window start here================================
main_window = tk.Tk()
#lbl.pack()
#pprint(dict(lbl))
#root = tk.Tk()
#T.insert(tk.END, "MM32 main details\navailable here\n")
#main_window.add_command(label="Clear screen  |", command=clear)
app = Application(main_window)
#img2 = ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(main_window, image = img2)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
#panel.place(x=0,y=0)
T = tk.Text(main_window,width=100, height=30)
T.pack()
app.mainloop()
#===============================main window end here=====================================





