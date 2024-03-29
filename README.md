# MMM Monitors Methane ✈️
Monitoring programs for an aerial methane monitor.  

![progress.png](https://raw.githubusercontent.com/Earth13wells/Methane/main/Images/progress.png)   

#### Left shows initial testing versus final hardware results    

### Included Program Files 🎪  
#### ~~~~~~~~~~~~~~~~~~~~~~  
* README.md  
* arduino.ino
* heatmap.py  
* Report.py    
* WindowsMap.p    
* clean.sh  

### Included 3D Designs 🗼  
#### ~~~~~~~~~~~~~~~~~~~~~~  
* GPSBracket.scad
* sdMount.scad
* undercarriage.scad


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
* Writes to output.csv file on micro sd card    
* Runs on Arduino Nano ✈️    
##### clean.sh    
* Formats output.    
* Runs on Data analysis computer 🔌    
##### heatmap.py   
* Generates graphs and other useful data visualisation    
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

### Usage
#### ~~~~~
##### Heatmap
- Navigate to the heatmap directory
- Run: python heatmapV2.py [filename]
- Where Ede {filename} is a cleaned file in the data directory
- Optionally, you can include -l or -s for line colour and point size respectively
- eg. python heatmapV2.py output.txt -l blue -s 6    
![Heatmap Picture](https://raw.githubusercontent.com/Earth13wells/Methane/main/Images/heatmap_preview.png)
![Image of  drone w/ hardware](https://raw.githubusercontent.com/Earth13wells/Methane/main/Images/image1.jpg)   

### Contributing 🕸️    
#### ~~~~~~~~~~~~
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
