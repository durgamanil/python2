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

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="MM32F_SERIES",variable=mayoVar )
mb.menu.add_checkbutton ( label="MM32L_SERIES",variable=ketchVar )
mb.menu.add_checkbutton ( label="MM32SPIN_SERIES",variable=ketchVar )
mb.menu.add_checkbutton ( label="MM32W_SERIES",variable=ketchVar )
mb.menu.add_checkbutton ( label="MM32P_SERIES",variable=ketchVar )

mb.pack()
gui.mainloop()