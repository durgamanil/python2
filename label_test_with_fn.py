# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:29:38 2020

@author: Onyx1
"""



import tkinter as tk
#ARM Cortex M0",48,16,2,16,1,5,2,1,1,1,8,0,0,"QFN20"
mc_list=[
        {
                "id":"mm32f003nw",
                "processor":"ARM Cortex M0",
                "frequency":"48",
                "flash":"16",
                "ram":"2",
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"1",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"8",
                "eeprom":"0",
                "pack":"QFN20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":"",
                
                },
              {
                "id":"mm32f003tw"
                 "processor":"ARM Cortex M0",
                "frequency":"48",
                "flash":"16",
                "ram":"2",
                "gpio":"16",
                "adv_tm":"1",
                "gptm":"5",
                "wdg":"2",
                "rtc":"1",
                "uart":"1",
                "i2c":"1",
                "spi":"1",
                "adc":"8",
                "eeprom":"0",
                "pack":"QFN20",
                "dac":"",
                "usb":"",
                "can":"",
                "sdio":"",
                "comp":"",
                "aes":"",
                "trng":"",
                
                }
        
        ]

def details(processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom="-",pack="-",dac="-",usb="",can="",sdio=0,comp=0,aes=0,trng=0,**para):
    T.insert(tk.END, "===========================================================================\n")
    T.insert(tk.END, "Max speed in hz\t\tFLASH\t\tRAM\t\tGPIO\n")
    T.insert(tk.END, "=========================================================================\n")
    T.insert(tk.END,"PROCESSOR::======>{}\n".format(processor))
    T.insert(tk.END,"Frequency Max speed ::====>{}Mhz\n".format(frequency))
    T.insert(tk.END,"FLASH::====>{}KBytes\n".format(flash))
    T.insert(tk.END,"RAM::====>{}KBytes\n".format(ram))
    T.insert(tk.END,"GPIO::====>{}Pins\n".format(gpio))
    T.insert(tk.END,"Advanced timer::====>{}\n".format(adv_tm))
    T.insert(tk.END,"GPTM::====>{}\n".format(gptm))
    T.insert(tk.END,"WDG::====>{}\n".format(wdg))
    T.insert(tk.END,"RTC::====>{}\n".format(rtc))
    T.insert(tk.END,"UART::====>{}\n".format(uart))
    T.insert(tk.END,"I2C::====>{}\n".format(i2c))
    T.insert(tk.END,"SPI::====>{}\n".format(spi)) 
    T.insert(tk.END,"ADC::====>{}x12bit\n".format(adc))
    T.insert(tk.END,"EEPROM::====>{}KBytes\n".format(eeprom))
    T.insert(tk.END,"PACk::====>{}\n".format(pack))
    T.insert(tk.END,"DAC::====>{}\n".format(dac))
    T.insert(tk.END,"USB::====>{}\n".format(usb))
    T.insert(tk.END,"CAN::====>{}\n".format(can))
    T.insert(tk.END,"SDIO::====>{}\n".format(sdio))
    T.insert(tk.END,"COMP::====>{}\n".format(comp))
    T.insert(tk.END,"AES::====>{}\n".format(aes))
    T.insert(tk.END,"TRNG::====>{}\n".format(trng))
    T.insert(tk.END,"===========================================================================\n")
    

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#processor,frequency,flash,ram,gpio,adv_tm,gptm,wdg,rtc,uart,i2c,spi,adc,eeprom="-",pack="-",dac="-",usb="",can="",sdio=0,comp=0,aes=0,trng=0

#####------------------main program start_here-----------------
master = tk.Tk()
processor=Label(master,text="Processor",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=0,sticky=N+S+E+W)
frequency=Label(master,text="Frequency",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=1,sticky=N+S+E+W)
flash=Label(master,text="Flash",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=2,sticky=N+S+E+W)
ram=Label(master,text="RAM",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=3,sticky=N+S+E+W)
gpio=Label(master,text="GPIO",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=4,sticky=N+S+E+W)
adv_tm=Label(master,text="Adv TM",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=5,sticky=N+S+E+W)
gptm=Label(master,text="GPTM",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=6,sticky=N+S+E+W)
wdg=Label(master,text="WDG",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=7,sticky=N+S+E+W)
rtc=Label(master,text="RTC",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=8,sticky=N+S+E+W)
uart=Label(master,text="UART",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=9,sticky=N+S+E+W)
i2c=Label(master,text="I2C",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=10,sticky=N+S+E+W)
spi=Label(master,text="SPI",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=11,sticky=N+S+E+W)
adc=Label(master,text="ADC",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=12,sticky=N+S+E+W)
eeprom=Label(master,text="EEPROM",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=13,sticky=N+S+E+W)
pack=Label(master,text="PACK",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=14,sticky=N+S+E+W)
dac=Label(master,text="DAC",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=15,sticky=N+S+E+W)
usb=Label(master,text="USB",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=16,sticky=N+S+E+W)
can=Label(master,text="CAN",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=17,sticky=N+S+E+W)
sdio=Label(master,text="SDIO",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=18,sticky=N+S+E+W)
comp=Label(master,text="COMP",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=19,sticky=N+S+E+W)
aes=Label(master,text="AES",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=20,sticky=N+S+E+W)
trng=Label(master,text="TRNG",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove").grid(row=0,column=21,sticky=N+S+E+W)

tk.Label(master,text="First Name").grid(row=2)
tk.Label(master,text="Last Name").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=4, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=4, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
print("end of the program\n")