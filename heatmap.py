#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#
import math
#
import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
#
import pandas as pd
import csv
import numpy as np
import random
import time
#
dtype=object
#BUTTONS
class ButtonWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="MMM Monitors Methane - Drone")

		# the label takes up the top 3 cells, and the button takes up the middle row.
		# Initialize 3x3 grid
		grid = Gtk.Grid()
		self.add(grid)

		self.set_border_width(5)
		# Make label
		label = Gtk.Label()
		label.set_size_request(1, 1) # Set label size
		label.set_text("Thank you for choosing MMM")
		grid.attach(label, 0, 0, 3, 1) # x pos, y pos, width, height (in terms of 3x3 grid)
#
		# Make buttons
		button = Gtk.Button.new_with_label("Graph!")
		button.set_size_request(3, 1)
		button.connect("clicked", self.graph) # Event "graph" on click
		grid.attach_next_to(button, label, Gtk.PositionType.BOTTOM, 1, 1) # Put the button below the label
#
		# Make dropdown
		# Create list to go into the dropdown
		combo = Gtk.ListStore(int, str)
		combo.append([0, "Select Graph to Display..."])
		combo.append([1, "Temperature"])
		combo.append([2, "Humidity"])
		combo.append([3, "Methane"])
		combo.append([4, "Pressure (KPa)"])
		#combo.append([5, "Longitude"])
		#combo.append([6, "Altitude"])
#
		# Put the list into the box
		dropdown = Gtk.ComboBox.new_with_model_and_entry(combo)
		dropdown.connect("changed", self.on_name_combo_changed)
		dropdown.set_entry_text_column(1)
		dropdown.set_active(0)
		grid.attach_next_to(dropdown, button, Gtk.PositionType.BOTTOM, 1, 1)

		checkbox = Gtk.CheckButton.new_with_label("Test")
		grid.attach_next_to(checkbox, dropdown, Gtk.PositionType.BOTTOM, 1, 1)
#
	def graph(self, button):
		Gtk.main_quit()
#
	#sets "which" to the index of the option
	def on_name_combo_changed(self, combo):
		global which
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			which = model[tree_iter][0]
#
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
#END OF BUTTONS
#
if (which != 0):
	fig = plt.figure()
if (which == 1):
	ax1 = fig.gca(projection='3d')
elif (which == 2):
	ax2 = fig.gca(projection='3d')
elif (which == 3):
	ax3 = fig.gca(projection='3d')
elif (which == 4):
	ax4 = fig.gca(projection='3d')
#
# If this works im drinking several glasses of vodka
#
results = []
with open("./Data/transposedcardata.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

results = np.array(results)
methane = results[0][2:]
humidity = results[1][2:]
temperature = results[2][2:]
pressure = results[3][2:]
altitude = results[4][2:]
latitude = results[5][2:]
longitude = results[6][2:]

latmin = np.floor(latitude.min())
latmax = np.ceil(latitude.max())
lonmin = np.floor(longitude.min())
lonmax = np.ceil(longitude.max())

if (latmax - latmin > lonmax - lonmin):
	x1 = latmin
	x2 = latmax
	y1 = lonmin
	y2 = lonmin + (latmax - latmin)
else:
	x1 = latmin
	x2 = latmin + (lonmax - lonmin)
	y1 = lonmin
	y2 = lonmax
#
# Plot the data to three different plots
if (which == 1):
	ax1.scatter(latitude, longitude, altitude, c=temperature, s=1)
<<<<<<< HEAD
	ax1.set_xlim3d(x1, x2)
	ax1.set_ylim3d(y1, y2)
=======
>>>>>>> 90e49c87257d7edb40fa565628461a3156e37024
	ax1.set_title("Temperature Heatmap")
	ax1.set_xlabel("x (m)")
	ax1.set_ylabel("y (m)")
	ax1.set_zlabel("altitude (m)")
if (which == 2):
	ax2.scatter(latitude, longitude, altitude, c=humidity, s=1)
<<<<<<< HEAD
	ax2.set_xlim3d(x1, x2)
	ax2.set_ylim3d(y1, y2)
=======
>>>>>>> 90e49c87257d7edb40fa565628461a3156e37024
	ax2.set_title("Humidity Heatmap")
	ax2.set_xlabel("x (m)")
	ax2.set_ylabel("y (m)")
	ax2.set_zlabel("altitude (m)")
if (which == 3):
	ax3.scatter(latitude, longitude, altitude, c=methane, s=1)
<<<<<<< HEAD
	ax3.set_xlim3d(x1, x2)
	ax3.set_ylim3d(y1, y2)
=======
>>>>>>> 90e49c87257d7edb40fa565628461a3156e37024
	ax3.set_title("Methane Heatmap")
	ax3.set_xlabel("x (m)")
	ax3.set_ylabel("y (m)")
	ax3.set_zlabel("altitude (m)")
if (which == 4):
	ax4.scatter(latitude, longitude, altitude, c=pressure, s=1)
<<<<<<< HEAD
	ax4.set_xlim3d(x1, x2)
	ax4.set_ylim3d(y1, y2)
=======
>>>>>>> 90e49c87257d7edb40fa565628461a3156e37024
	ax4.set_title("Methane Heatmap")
	ax4.set_xlabel("x (m)")
	ax4.set_ylabel("y (m)")
	ax4.set_zlabel("altitude (m)")
plt.show()
#
