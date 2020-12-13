#!/usr/bin/env python3
import Serial
from threading import Thread
from picamera import PiCamera
from sense_hat import SenseHat
from time import sleep, strftime

def ReadArdiuno():
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
w = open("output.txt", "a")
w.write('Pressure, Temp, Humidity, Time')
w.write("\n")
w.close()
        
cycle = int(input("Number of cycles: "))
for x in range (0,cycle,1):
#
        tr = Thread(target = ReadArduino, args=(), name="ardiunodata"+x)
        tr.start()

        output =  str( [ sense.get_pressure(), sense.get_temperature(), sense.get_humidity(), strftime("%H:%M:%S") ] )
        output = str(output)
#
	#r = open("/path/to/usb1/output1.csv", "a") #uncomment when usb storage is used
	#m = open("/path/to/usb2/output2.csv", "a") #These can probably be done all at once?
	#p = open("/path/to/usb3/output3.csv", "a")
        w.write('Pressure, Temp, Humidity, Time')
        w.write(output)
        w.write("\n")
        w.close()
	#r.close() #uncomment when usb storage is used
	#m.close() # ^^
	#p.close() # ^^
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
#
# LGPL-2.0  :  GNU Library General Public License v2 only
