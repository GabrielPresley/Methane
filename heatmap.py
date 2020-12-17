import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import math

import matplotlib.use
use('GTK3Agg')
import matplotlib.pyplot as plt

import pandas as pd
import random
import time
#
#BUTTONS
class ButtonWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Methane - Drone")
		
		"""
		From what I get, basically it uses a 3x3 grid and things are added to this grid.
		So the label takes up the top 3 cells, and the buttons take up the middle row.
		"""
		
		# Initialize 3x3 grid (I think)
		grid = Gtk.Grid()
		self.add(grid)

		self.set_border_width(5)
		# Make label
		label = Gtk.Label()
		label.set_size_request(900, 50) # Set label size
		label.set_text("Thank you for choosing Methane")
		grid.attach(label, 0, 0, 3, 1) # x pos, y pos, width, height (in terms of 3x3 grid)
#
		# Make buttons
		button1 = Gtk.Button.new_with_label("Temperature")
		button1.set_size_request(300, 200)
		button1.connect("clicked", self.temp) # Event "temp" on click
		grid.attach_next_to(button1, label, Gtk.PositionType.BOTTOM, 1, 1) # Put the button below the label
#
		button2 = Gtk.Button.new_with_label("Humidity")
		button2.set_size_request(300, 200)
		button2.connect("clicked", self.humid)
		grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 1, 1) # Put the button next to button1
#
		button3 = Gtk.Button.new_with_label("Methane")
		button3.set_size_request(300, 200)
		button3.connect("clicked", self.methane)
		grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 1, 1) # Put the button next to button2
#
		# Make dropdown
		# Create list to go into the dropdown
		combo = Gtk.ListStore(int, str)
		combo.append([0, "Select Graph to Display..."])
		combo.append([1, "Temperature"])
		combo.append([2, "Humidity"])
		combo.append([3, "Methane"])
#
		# Put the list into the box. I'm too lazy to explain all of it
		dropdown = Gtk.ComboBox.new_with_model_and_entry(combo)
		dropdown.connect("changed", self.on_name_combo_changed)
		dropdown.set_entry_text_column(1)
		dropdown.set_active(0)
		grid.attach_next_to(dropdown, button2, Gtk.PositionType.BOTTOM, 1, 1)
#
	def temp(self, button):
		global which
		which =  1
		Gtk.main_quit()
#
	def humid(self, button):
		global which
		which =  2
		Gtk.main_quit()
#
	def methane(self, button):
		global which
		which =  3
		Gtk.main_quit()
#
	# I don't really know how it works but it basically sets "which" to the index of the option
	def on_name_combo_changed(self, combo):
		global which
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			which = model[tree_iter][0]
		Gtk.main_quit()
		
#
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
print(which)
#END OF BUTTONS
#
fig = plt.figure()
#
if (which == 1):
	ax1 = fig.gca(projection='3d')
elif (which == 2):
	ax2 = fig.gca(projection='3d')
elif (which == 2):
	ax3 = fig.gca(projection='3d')
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
# Plot the data to three different plots
if (which == 1):
	ax1.scatter(x, y, altitude, c=temperature)
	ax1.set_title("Temperature Heatmap")
	ax1.set_xlabel("x (m)")
	ax1.set_ylabel("y (m)")
	ax1.set_zlabel("altitude (m)")
	ax1.view_init(35, 190)
if (which == 2):
	ax2.scatter(x, y, altitude, c=humidity)
	ax2.set_title("Humidity Heatmap")
	ax2.set_xlabel("x (m)")
	ax2.set_ylabel("y (m)")
	ax2.set_zlabel("altitude (m)")
	ax2.view_init(35, 190)
if (which == 3):
	ax3.scatter(x, y, altitude, c=methane)
	ax3.set_title("Methane Heatmap")
	ax3.set_xlabel("x (m)")
	ax3.set_ylabel("y (m)")
	ax3.set_zlabel("altitude (m)")
	ax3.view_init(30, 135)
plt.show()
#
