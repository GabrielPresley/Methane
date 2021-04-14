# MMM Monitors Methane ✈️
Monitoring programs for an aerial methane monitor.  

### Included Program Files 🎪  
#### ~~~~~~~~~~~~~~~~~~~~~~  
* README.md  
* arduino.ino
* heatmapV2.py  
* WindowsMap.py    
* clean.sh  
* Report.py    

### Introduction ✍️
#### ~~~~~~~~~~~~

&nbsp;&nbsp;&nbsp;&nbsp; Air pollution is a dire health and
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
* Writes to output.csv file    
* Runs on Arduino Nano ✈️
<<<<<<< HEAD
=======
##### raspberry.py    
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
>>>>>>> testing
##### clean.sh    
* Formats output.
* Runs on Data analysis computer 🔌
##### heatmapV2.py   
* Generates heat map of all data    
* Runs on data analysis computer 🔌   
##### Report.py   
* Generates a small data summary 📝    
* Runs on Data analysis computer 🔌
### Dependencies 🏗️
#### ~~~~~~~~~~~~
##### Python
* csv    
* gi (Gtk, Gio)    
* math    
* matplotlib (FigureCanvasGTK3Agg, Figure)    
* numpy    
* pandas     
* time (sleep, strftime)    

##### C++
* Wire.h    
* SD.h    
* SPI.h    
* Adafruit_Sensor.h    
* Adafruit_BME280.h     

### Install ⬇️
#### ~~~~~~~
* Flash arduino.ino to Arduino Nano    

### Contributing 🕸️
#### ~~~~~~~~~~~~
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
