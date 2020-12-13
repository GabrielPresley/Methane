#!/usr/bin/env python3
import serial
from threading import Thread
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep, strftime
from shutil import copyfile
#
camera = PiCamera()
sense = SenseHat()
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
                wait = False;
                return line
#
camera.resolution = (100, 100)
sense.clear() #PRY 0
#
w.write('Pressure,Temp,Humidity,Time')
w.write("\n")
#
cycle = int(input("Number of cycles: "))
for x in range (0,cycle,1):
#
        y = str(x)
        tr = Thread(target = ReadArduino, args=(), name="ardiunodata"+y)
        tr.start()
#
        output =  str( [ sense.get_pressure(), sense.get_temperature(), sense.get_humidity(), strftime("%H:%M:%S") ] )
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
            #for a in range (1,3):
                #copyfile('output.txt' '/path/to/usb5s/output_%s.csv' % (a, a))
                #Also need to do images to at least on drive.
#
