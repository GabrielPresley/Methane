# Methane
Monitoring programs for an aerial methane monitor.  
  
### Included Program Files  
#### ~~~~~~~~~~~~~~~~~~~~~~  
* README.md  
* cam.py  
* sensehat.py  
* clean.sh  
### Introduction
#### ~~~~~~~~~~~~

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Air pollution is a dire health and environmental threat at the forefront of humanity's concerns. As a result, there have been many studies focused on developing different environmental monitoring methods. Floating air monitors and towers that are currently being employed are efficient for data collection but are difficult to move to new places and air monitoring drones, although effective, can be quite expensive and are limited by their battery life. Theoretically, one can create a more effective drone for environmental monitoring by using a symmetrical fixed wing design. 

### Purpose
#### ~~~~~~~
##### arduino.ino
* Reads data from Methane sensor
* Runs on arduino
##### arduino-pi.py
* Current testing file for arduino > pi communication
* Takes readings from arduino and sends to RPi
* Runs on RPi
##### sensehat.py    
* Main data collection program 
* Responsible for photos
* Writes to output.txt  
* Collects Pressure, Temperature, Humidity, and time in form:  
* ```[1004.05615234375, 26.88888931274414, 44.61138916015625, '18:07:30']  ```
* Runs on RPi
##### clean.sh    
* Writes to cleanoutput.txt  
* Formats output.txt in form:  
* Pressure,              temp,              Humidity,              time  
* ``` [1004.05615234375    26.88888931274414    44.61138916015625    '18:07:30']  ```
* Runs on RPi

### Dependencies 
#### ~~~~~~~~~~~~
##### Python
* time
* SenseHat
* PiCamera

### Install
#### ~~~~~~~
* Download all files to ~/ on RPi
* Flash arduino.ino to Arduino Nano

### Contributing
#### ~~~~~~~~~~~~
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
