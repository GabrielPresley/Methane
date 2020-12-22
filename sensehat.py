#!/usr/bin/env python3
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

import serial
from picamera import PiCamera as camera
from sense_hat import SenseHat as sense
from shutil import copyfile
from threading import Thread
from time import sleep, strftime
#
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
w = open("output.csv", "a")
#
def ReadArduino():
    if __name__ == '__main__':
        ser.flush()
        wait = True
        while wait:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                wait = False
                return line
#
camera.resolution = (100, 100)
#
w.write('Pressure,Temp,Humidity,Time' "\n")
#
cycle = int(input("Number of cycles: "))
for x in range (0,cycle,1):
#
        y = str(x)
        tr = Thread(target = ReadArduino, args=(), name="ardiunodata"+y)
        tr.start()
#
        output =  str( [ sense.get_pressure(sense), sense.get_temperature(), sense.get_humidity(), strftime("%H:%M:%S") ] )
        output = str(output)
#
        w.write('Pressure, Temp, Humidity, Time')
        w.write(output)
        w.write("\n")
#
        sleep(1)
#
        o = sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]
        print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~", x)
#
        if (x % 5 == 0 ):
            t = strftime("%H:%M:%S")
            camera.capture('/home/pi/images/image_%s_%s.jpg' % (t, x))
            if (x % 100 == 0):
                for a in range (1,3):
                    copyfile('output.txt' '/path/to/usb%s/output_%s.csv' % (a, a))
                    #Also need to do images to at least one drive.
#
