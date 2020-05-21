
from tkinter import *
import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom="-",pack="-",dac="-",usb="",can="",sdio=0,comp=0,aes=0,trng=0

#####------------------main program start_here-----------------
master = tk.Tk()
#scrollbar = Scrollbar(master)
#scrollbar.pack( side = RIGHT, fill=Y )

#mylist = Listbox(root, yscrollcommand = scrollbar.set )
processor=Label(master,text="processor",bg="black",fg="white").grid(row=0,column=0,sticky=N+S+E+W)
frequency=Label(master,text="frequency",bg="white",fg="black").grid(row=0,column=1,sticky=N+S+E+W)
flash=Label(master,text="flash",bg="black",fg="white").grid(row=0,column=2,sticky=N+S+E+W)
ram=Label(master,text="ram",bg="white",fg="black").grid(row=0,column=3,sticky=N+S+E+W)
gpio=Label(master,text="gpio",bg="black",fg="white").grid(row=0,column=4,sticky=N+S+E+W)
adv_tm=Label(master,text="adv_tm",bg="black",fg="white").grid(row=0,column=5,sticky=N+S+E+W)
gptm=Label(master,text="gptm",bg="black",fg="white").grid(row=0,column=6,sticky=N+S+E+W)
wdg=Label(master,text="wdg",bg="black",fg="white").grid(row=0,column=7,sticky=N+S+E+W)
rtc=Label(master,text="rtc",bg="black",fg="white").grid(row=0,column=8,sticky=N+S+E+W)
uart=Label(master,text="uart",bg="black",fg="white").grid(row=0,column=9,sticky=N+S+E+W)
i2c=Label(master,text="i2c",bg="black",fg="white").grid(row=0,column=10,sticky=N+S+E+W)
spi=Label(master,text="spi",bg="black",fg="white").grid(row=0,column=11,sticky=N+S+E+W)
adc=Label(master,text="adc",bg="black",fg="white").grid(row=0,column=12,sticky=N+S+E+W)
eeprom=Label(master,text="eeprom",bg="black",fg="white").grid(row=0,column=13,sticky=N+S+E+W)
pack=Label(master,text="pack",bg="black",fg="white").grid(row=0,column=14,sticky=N+S+E+W)
dac=Label(master,text="dac",bg="black",fg="white").grid(row=0,column=15,sticky=N+S+E+W)
usb=Label(master,text="usb",bg="black",fg="white").grid(row=0,column=16,sticky=N+S+E+W)
can=Label(master,text="can",bg="black",fg="white").grid(row=0,column=17,sticky=N+S+E+W)
sdio=Label(master,text="sdio",bg="black",fg="white").grid(row=0,column=18,sticky=N+S+E+W)
comp=Label(master,text="comp",bg="black",fg="white").grid(row=0,column=19,sticky=N+S+E+W)
aes=Label(master,text="aes",bg="black",fg="white").grid(row=0,column=20,sticky=N+S+E+W)
trng=Label(master,text="trng",bg="black",fg="white").grid(row=0,column=21,sticky=N+S+E+W)



#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )
tk.mainloop()
print("end of the program\n")