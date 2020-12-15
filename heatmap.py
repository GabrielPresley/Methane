import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import math

import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt

import pandas as pd
import random
import time
#
#BUTTONS
class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Methane - Drone")
        self.set_border_width(10)
#
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)
#
        button = Gtk.Button.new_with_label("Temperature")
        button.connect("clicked", self.temp)
        hbox.pack_start(button, True, True, 0)
#
        button = Gtk.Button.new_with_label("Humidity")
        button.connect("clicked", self.humid)
        hbox.pack_start(button, True, True, 0)
#
        button = Gtk.Button.new_with_label("Methane")
        button.connect("clicked", self.methane)
        hbox.pack_start(button, True, True, 0)
#
    def temp(self, button):
        global which
        which =  "temp"
        Gtk.main_quit()
#
    def humid(self, button):
        global which
        which =  "humidity"
        Gtk.main_quit()
#
    def methane(self, button):
        global which
        which =  "methane"
        Gtk.main_quit()
#
#
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
print(which)
#END OF BUTTONS

if (which == "temp"):
    fig1 = plt.figure()
    ax1 = fig1.gca(projection='3d')
elif (which == "humidity"):
    fig2 = plt.figure()
    ax2 = fig2.gca(projection='3d')
elif (which == "methane"):
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111, projection='3d')

#
# Remove once we have GPS data
x = []
y = []
#
# Load data. I used the raw data from output.csv for testing
data = pd.read_csv('DroneTestData.csv')
#
altitude = []
#
# Remove once we have GPS data
for i in range(3044):
    x.append(i % 50)
    y.append(math.floor(i / 50))
#
# Columns = pressure, temperature, humidity, time(not used), methane(need methane data), x(need GPS data), y(need GPS data)
pressure = data.iloc[:, 0].tolist()
temperature = data.iloc[:,1].tolist()
humidity = data.iloc[:,2].tolist()
#
# Add once we have GPS and methane data
#methane = data.iloc[:,4].tolist()
#x = data.iloc[:,5].tolist()
#y = data.iloc[:,6].tolist()
#
# Get altitude from pressure
for i in range(len(pressure)):
    altitude.append((((1013.25/pressure[i])**(1/5.257)-1)*(temperature[i]+273.15))/0.0065)
#
# Plot the data to two different plots
if (which == "temp"):
    ax1.scatter(x, y, altitude, c=temperature)
    ax1.set_title("Temperature Heatmap")
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    ax1.set_zlabel("altitude (m)")
    ax1.view_init(35, 190)
if (which == "humidity"):
    ax2.scatter(x, y, altitude, c=humidity)
    ax2.set_title("Humidity Heatmap")
    ax2.set_xlabel("x (m)")
    ax2.set_ylabel("y (m)")
    ax2.set_zlabel("altitude (m)")
    ax2.view_init(35, 190)
if (which == "methane"):
    ax3.scatter(x, y, altitude, c=methane)
    ax3.set_title("Methane Heatmap")
    ax3.set_xlabel("x (m)")
    ax3.set_ylabel("y (m)")
    ax3.set_zlabel("altitude (m)")
    ax3.text2D(0.05, 0.07, "Colour = Methane")
    ax3.view_init(30, 135)
plt.show()
#
