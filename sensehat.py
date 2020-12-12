#!/usr/bin/env python3
import time, Serial
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep, strftime
#
camera = PiCamera()
camera.resolution = (100, 100)
#
sense = SenseHat()
sense.clear() #PRY 0
#
cycle = int(input("Number of cycles: "))
for x in range (0,cycle,1):
#
        output =  [sense.get_pressure(), sense.get_temperature(), sense.get_humidity(), time.strftime("%H:%M:%S")]
        output = str(output)
#
        w = open("output.txt", "a")
        w.write('Pressure, Temp, Humidity, Time')
        w.write(output)
        w.write("\n")
        w.close()
#
        time.sleep(1)
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
#
# LGPL-2.0  :  GNU Library General Public License v2 only
