import serial
import time

arduinoData=serial.Serial('com5',9600)

def buzz_on():
    arduinoData.write(b'1')

def buzz_off():
    arduinoData.write(b'0')

while 1:
     buzz_on()
     time.sleep(1)
     buzz_off()
     time.sleep(2)
     print("Done")