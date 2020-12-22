#!/usr/bin/env python3
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

#imports required moduals
import serial
from picamera import PiCamera
from sense_hat import SenseHat
from shutil import copyfile
from threading import Thread
from time import sleep, strftime
#
#opens the serial port to communicate with the arduino
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#opens the file to write data to
w = open("output.csv", "a")
#
#defines the function to read the ardiuno's response
def ReadArduino():
    if __name__ == '__main__':
        ser.flush()
        wait = True
        #repeats until a message is recieved from the arduino
        while wait:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                wait = False
                print(line);
                
                return line
#
#defines an instance of the PiCamera class under camera
camera = PiCamera()

#sets the cameras resolution
camera.resolution = (100, 100)
#
#writes the titles to the data file
w.write('Pressure,Temp,Humidity,Time' "\n")

#defines and instance fo the SenseHat class under sense
sense = SenseHat()
#
#determines the number of cycles from the user
cycle = int(input("Number of cycles: "))

#repeats for each cycle
for x in range (0,cycle,1):
#
        #starts a new thread which waits for a reading from the arduino
        y = str(x)
        tr = Thread(target = ReadArduino, args=(), name="ardiunodata"+y)
        tr.start()
#
        #defines output as the string for the array of the data from the sensehat and the time
        output =  str( [ sense.get_pressure(), sense.get_temperature(), sense.get_humidity(), strftime("%H:%M:%S") ] )
        output = str(output)
#  
        #writes the output to the data file along with its titles
        w.write('Pressure, Temp, Humidity, Time')
        w.write(output)
        w.write("\n")
#       
        #waits one second
        sleep(1)
#
        #records the orientation of the pi and prints it to the terminal
        o = sense.get_orientation()
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]
        print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~", x)
#
        #takes a picture every 5 cycles
        if (x % 5 == 0 ):
        
            #determines the time
            t = strftime("%H:%M:%S")
            n = "/home/pi/images/image_%s_%s.jpg" % (t, x)
            #takes a photo and saves it with the time and number
            camera.capture(n)
            
            #every 100 cycles it backs up the data to a usb drive
            if (x % 100 == 0):
                for a in range (1,3):
                    #please note the pass here is temporary and meant to be removed when we have usbs to copy to
                    pass
                    #copyfile('output.txt' '/path/to/usb%s/output_%s.csv' % (a, a))
                    #Also need to do images to at least one drive.
#