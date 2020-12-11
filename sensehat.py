import time
from sense_hat import SenseHat
#
sense = SenseHat()
sense.clear() #PRY 0
#
cycle = input("Number of cycles: ")
for x in range (0,cycle,1):
#
        output =  [sense.get_pressure(), sense.get_temperature(), sense.get_humidity(), time.strftime("%H:%M:%S")]
        output = str(output)
#
        w = open("output.txt", "a")
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
# LGPL-2.0  :  GNU Library General Public License v2 only
