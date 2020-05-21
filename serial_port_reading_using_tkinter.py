from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import ttk
import serial.tools.list_ports
import sys
import glob
import serial
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk, Image
from pprint import pprint
#scr = Tk()
path = 'F:\my_workspace\python_workspace\onyx_tool\onyx-logo.png'

# --- functions ---

def serial_ports():    
    return serial.tools.list_ports.comports()

def on_select(event=None):
    # get selection from event    
    print("event.widget:", event.widget.get())
    # or get selection directly from combobox
    print("comboboxes: ", cb.get())

# --- main ---

root = tk.Tk()
root.title("ONYX COM TOOL")
img2 = ImageTk.PhotoImage(Image.open(path))
panel=tk.Label(root, image = img2)
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.place(x=0,y=0)

cb = ttk.Combobox(root, values=serial_ports(),width=50, height=20)
cb.pack()


# assign function to combobox
cb.bind('<<ComboboxSelected>>', on_select)

T = tk.Text(root,width=50, height=20)
T.pack()
#print(on_select)
cb.bind('<<ComboboxSelected>>', on_select)
#T.insert(tk.END, "comport\n".format(values))
#T.insert(tk.END, "COM-PORT:".format(cb.bind('<<ComboboxSelected>>', on_select)))
buttom_status=Label(root,text = "@2020-copyright protected from onyx components and systems",bd=1,relief=SUNKEN,anchor=W)
buttom_status.pack(side = BOTTOM, fill = X)

root.mainloop()