

from tkinter import *

mm32=tk.Tk()

topframe = Frame(mm32)
topframe.pack()
bottomframe=Frame(mm32)
bottomframe.pack(side=BOTTOM)

button1=Button(topframe,text="MM32F",fg="red",font=('Helvetica', 15))
button2=Button(topframe,text="MM32L",fg="red",font=('Helvetica', 15))
button3=Button(topframe,text="MM32SPIN",fg="red",font=('Helvetica', 15))
button4=Button(topframe,text="MM32W",fg="red",font=('Helvetica', 15))
button5=Button(topframe,text="MM32P",fg="red",font=('Helvetica', 15))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

mm32.mainloop()