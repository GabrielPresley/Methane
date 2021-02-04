# MMM Monitors Methane ✈️
Monitoring programs for an aerial methane monitor.  

### Included Program Files 🎪  
#### ~~~~~~~~~~~~~~~~~~~~~~  
* README.md  
* arduino.ino
* heatmap.py  
* WindowsMap.py    
* clean.sh  
* raspberry.py    

### Introduction ✍️
#### ~~~~~~~~~~~~

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Air pollution is a dire health and
environmental threat at the forefront of humanity's concerns. As a result, there
 have been many studies focused on developing different environmental monitoring
  methods. Floating air monitors and towers that are currently being employed
  are efficient for data collection but are difficult to move to new places and
   air monitoring drones, although effective, can be quite expensive and are
   limited by their battery life. Theoretically, one can create a more effective
    drone for environmental monitoring by using a symmetrical fixed wing design.

### Purpose 🥅
#### ~~~~~~~
##### arduino.ino
* Main data collection program
* Reads data from Methane sensor
* Reads data from BME280 sensor
* Reads data from GPS sensor
* Runs on Arduino Nano ✈️
##### sensehat.py    
* Responsible for photos
* Responsible for arduino-pi communication
* Writes to output.csv in form   
```
Humidity (%) 30.83
Methane (PPM) 558.89
Temperature (*c) 29.12
Pressure (hPa) 989.71
Altitude (m) 198.05
```
* Runs on RPi 🛩️  
##### clean.sh    
* Writes to cleanoutput.txt  
* Formats output.txt in form:  
* Pressure,              temp,              Humidity,              time  
* ``` [1004.05615234375    26.88888931274414    44.61138916015625    '18:07:30']  ```  
* Runs on Data analysis computer 🔌
##### heatmap.py   
* Generates heat map of Methane data    
* Runs on data analysis computer 🔌      
### Dependencies 🏗️
#### ~~~~~~~~~~~~
##### Python
* PiCamera
* random
* SenseHat
* math
* matplotlib.pyplot
* pandas
* serial
* shutil
* threading
* time
##### C++
* Adafruit_GPS.h

### Install ⬇️
#### ~~~~~~~
* Download all files to ~/ on RPi
* Flash arduino.ino to Arduino Nano

### Contributing 🕸️
#### ~~~~~~~~~~~~
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
