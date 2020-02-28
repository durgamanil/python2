import serial
import time

sms = serial.Serial("COM116", baudrate=115200, timeout=1.0)

sms.write("AT+CPIN\r\n")
result=sms.read(100)
print(result)

sms.write('AT+CMGF=1\r\n')
result=sms.read(100)
sms(result)

phone.write('AT+CMGS="+918897520530"\r\n')
result=phone.read(100)
sms(result)