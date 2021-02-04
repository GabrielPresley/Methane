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
from time import sleep, strftime
from picamera import PiCamera
#
# open serial port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#
w = open("output.csv", "w")
#
arduinodata = ""
while arduinodata != "'":
    arduinodata = str(ser.read())
while True:
    arduinodata = str(ser.read())
    w.write(arduinodata)
