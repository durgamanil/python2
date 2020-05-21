

import tkinter as tk

OptionList = ['MM32F_SERIES', 'MM32L_SERIES', 'MM32SPIN_SERIES', 'MM32W_SERIES','MM32P_SERIES'
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=20, font=('Helvetica', 15))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))
    #if format(variable.get()) == "MM32F_SERIES"
    print("MM32F_SERIES")

variable.trace("w", callback)
app.mainloop()