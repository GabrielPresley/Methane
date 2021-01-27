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
#ser.open()
#camera = PiCamera()
#camera.resolution = (100, 100)
w = open("output.csv", "a")
#
for i in range(420):
    arduinodata = str(ser.read())
    w.write(arduinodata)
#    if (x % 5 == 0 ):
        #Updates time
#        t = strftime("%H:%M:%S")
        #takes a photo and saves it with the time and number
#        camera.capture(("/home/pi/images/image_%s_%s.jpg" % (t, x)))
    #every 100 cycles it backs up the data to a usb drive
#    if (x % 100 == 0):
#        for a in range (1,2):
#            copyfile('output.csv', 'pioutput/usb%s/output_%s.csv' % (a, a))
