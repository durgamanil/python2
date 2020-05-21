from tkinter import *
#import tkMessageBox
import tkinter
gui = Tk()
gui.configure(background="light green")
gui.title("MM32_MICROCONTROLLER_DATA")
gui.geometry("1024x768")


mb=  Menubutton ( gui, text="MM32_MICROCONTROLLER", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

FVar = IntVar()
LVar = IntVar()
SPINVar = IntVar()
WVar = IntVar()
PVar = IntVar()

mb.menu.add_checkbutton ( label="MM32F SERIES",variable=FVar )
mb.menu.add_checkbutton ( label="MM32L SERIES",variable=LVar )
mb.menu.add_checkbutton ( label="MM32SPIN SERIES",variable=SPINVar )
mb.menu.add_checkbutton ( label="MM32W SERIES",variable=WVar )
mb.menu.add_checkbutton ( label="MM32P SERIES",variable=PVar )

mb.pack()
gui.mainloop()