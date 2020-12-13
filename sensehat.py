#!/usr/bin/env python3
import Serial
from threading import Thread
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep, strftime
from shutil import copyfile
#
def ReadArdiuno():0
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.flush()
        wait = True
        while wait:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                wait = False;
#
camera = PiCamera()
camera.resolution = (100, 100)
#
sense = SenseHat()
sense.clear() #PRY 0
#
w = open("output.csv", "a")
w.write('Pressure,Temp,Humidity,Time')
w.write("\n")
#
cycle = int(input("Number of cycles: "))
for x in range (0,cycle,1):
#
        tr = Thread(target = ReadArduino, args=(), name="ardiunodata"+x)
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
            for a in range (1,3)
                #copyfile('output.txt' '/path/to/usb5s/output_%s.csv' % (a, a))
#
