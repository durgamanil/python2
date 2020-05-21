from tkinter import *
root = Tk()

one =Label(root,text="ONE",bg="red",fg="white")
one.pack()
two =Label(root,text="TWO",bg="green",fg="black")
two.pack(fill=X)
three =Label(root,text="THREE",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)


root.mainloop()
