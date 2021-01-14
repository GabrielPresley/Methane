#!/usr/bin/env python3
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

#import modules
import serial
from shutil import copyfile
from threading import Thread
from time import sleep, strftime

# open serial port
ser = serial('/dev/ttyUSB0', 9600, timeout=1)
ser.open()


while True:
    arduinodata = string(ser.read())
    print(arduinodata)
    pass

ser.close()
