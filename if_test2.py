# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:53:53 2019

@author: anil durgam
"""
def details(frequency,flash,ram,gpio,adv_tm,gptm,wdg,uart,i2c,spi,adc,pack,*para):
    print("=====================================================================================")
    print("Max speed in hz\t\tFLASH\t\tRAM\t\tGPIO")
    print("===================================================================================")
    print("Frequency Max speed ::====>{}Mhz".format(frequency))
    print("FLASH::====>{}KBytes".format(flash))
    print("RAM::====>{}KBytes".format(ram))
    print("GPIO::====>{}KBytes".format(gpio))
    print("Advanced timer::====>{}".format(adv_tm))
    print("GPTM::====>{}".format(gptm))
    print("WDG::====>{}".format(wdg))
    print("UART::====>{}".format(uart))
    print("I2C::====>{}".format(i2c))
    print("SPI::====>{}".format(spi)) 
    print("ADC::====>{}x12bit".format(adc))  
    print("PACk::====>{}".format(pack))  
    print("====================================================================================")
    
    
#while(1):
in1=input("enter mm32 microcontroller")
print(in1)
#====================================================================
if in1=="mm32f003nw":
        print("mm32f003nw is selected\n")
        details(48,16,2,16,1,5,2,1,1,1,8,"QFN20")   
#===================================================================
elif in1=="mm32f003tw":
   print("mm32f003tw selected\n")
   details(48,16,2,16,1,5,2,1,1,1,8,"TSSOP20")  
#===================================================================          
elif in1=="mm32f031f4p6":
    print("mm32f031f4p6 is selected\n")
    details(72,16,4,16,1,5,2,1,1,1,9,"TSSOP20")  
#===================================================================
elif in1=="mm32f031f4u6":
    print("mm32f031f4u6 is selected\n")
    details(72,16,4,16,1,5,2,1,1,1,9,"QFN20")  
#===================================================================
elif in1=="mm32f031k4u6":
    print("mm32f031 is selected\n")
    details(72,16,4,27,1,5,2,1,1,1,9,"QFN32") 
#===================================================================
elif in1=="mm32f031k4t6":
    print("mm32f031 is selected\n")
    details(72,16,4,25,1,5,2,1,1,1,9,"QFN32")
#===================================================================
elif in1=="mm32f031":
    print("mm32f031 is selected\n")
elif in1=="mm32f032":
    print("mm32f032 is selected\n")
elif in1=="mm32f103":
   print("mm32f103 is selected\n")
elif in1=="mm32l050":
   print("mm32l050 is selected\n")
elif in1=="mm32l051":
   print("mm32l051 is selected\n")
elif in1=="mm32l052":
    print("mm32l052 is selected\n")
elif in1=="mm32l061":
   print("mm32l061 is selected\n")
elif in1=="mm32l062":
   print("mm32l062 is selected\n")
elif in1=="mm32l072":
    print("mm32l072 is selected\n")
elif in1=="mm32l073":
   print("mm32l073 is selected\n")
elif in1=="mm32l362":
   print("mm32l362 is selected\n")
elif in1=="mm32l373":
    print("mm32l373 is selected\n")
elif in1=="mm32l384":
    print("mm32l384 is selected\n")
elif in1=="mm32l395":
    print("mm32l395 is selected\n")
elif in1=="mm32w051":
    print("mm32w051 is selected\n")
elif in1=="mm32w062":
    print("mm32w062 is selected\n")
elif in1=="mm32w073":
    print("mm32w073 is selected\n")
elif in1=="mm32w362":
    print("mm32w362 is selected\n")
elif in1=="mm32w373":
    print("mm32w373 is selected\n")
elif in1=="mm32w384":
    print("mm32w384 is selected\n")
elif in1=="mm32w395":
    print("mm32w395 is selected\n")
elif in1=="mm32SPIN":
    print("mm32SPIN is selected\n")
else :
    print("microcontroller is not in the given list")


