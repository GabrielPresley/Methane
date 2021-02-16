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
* Runs on Arduino Nano ✈️
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
##### clean.sh    
* Formats output.
* Runs on Data analysis computer 🔌
##### heatmap.py   
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
* picamera (PiCamera)    
* serial (*WARNING:* DO NOT INSTALL SERIAL; INSTEAD PYSERIAL)    
* shutil (copyfile)    
* time (sleep, strftime)    

##### C++
* Adafruit_BME280.h    
* Adafruit_Sensor.h    
* Wire.h    

### Install ⬇️
#### ~~~~~~~
* Download raspberry.py to ~/ on RPi.     
- (dont forget to add "python ~/raspberry.py" to your .bashrc)    
* Flash arduino.ino to Arduino Nano    

### Contributing 🕸️
#### ~~~~~~~~~~~~
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
