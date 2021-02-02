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
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
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
		self.set_border_width(10)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.add(box)


		# Set up figures
		fig1 = Figure()
		fig2 = Figure()
		fig3 = Figure()
		fig4 = Figure()
		ax1 = fig1.gca(projection='3d')
		ax2 = fig2.gca(projection='3d')
		ax3 = fig3.gca(projection='3d')
		ax4 = fig4.gca(projection='3d')

		# Open CSV and save into lists
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

		# Fix Scaling
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

		# Graph data
		ax1.scatter(latitude, longitude, altitude, c=methane, s=1)
		ax1.set_xlim3d(x1, x2)
		ax1.set_ylim3d(y1, y2)
		ax1.set_title("Methane Heatmap")
		ax1.set_xlabel("x (m)")
		ax1.set_ylabel("y (m)")
		ax1.set_zlabel("altitude (m)")

		ax2.scatter(latitude, longitude, altitude, c=humidity, s=1)
		ax2.set_xlim3d(x1, x2)
		ax2.set_ylim3d(y1, y2)
		ax2.set_title("Humidity Heatmap")
		ax2.set_xlabel("x (m)")
		ax2.set_ylabel("y (m)")
		ax2.set_zlabel("altitude (m)")

		ax3.scatter(latitude, longitude, altitude, c=temperature, s=1)
		ax3.set_xlim3d(x1, x2)
		ax3.set_ylim3d(y1, y2)
		ax3.set_title("Temperature Heatmap")
		ax3.set_xlabel("x (m)")
		ax3.set_ylabel("y (m)")
		ax3.set_zlabel("altitude (m)")

		ax4.scatter(latitude, longitude, altitude, c=pressure, s=1)
		ax4.set_xlim3d(x1, x2)
		ax4.set_ylim3d(y1, y2)
		ax4.set_title("Pressure Heatmap")
		ax4.set_xlabel("x (m)")
		ax4.set_ylabel("y (m)")
		ax4.set_zlabel("altitude (m)")

		#Create display
		main = Gtk.Stack()
		main.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		main.set_transition_duration(300)

		met = FigureCanvas(fig1)
		met.set_size_request(400, 400)
		main.add_titled(met, "methane", "Methane")

		hum = FigureCanvas(fig2)
		hum.set_size_request(400, 400)
		main.add_titled(hum, "methane", "Humidity")

		tem = FigureCanvas(fig3)
		tem.set_size_request(400, 400)
		main.add_titled(tem, "temperature", "Temperature")

		pre = FigureCanvas(fig4)
		pre.set_size_request(400, 400)
		main.add_titled(pre, "pressure", "Pressure")

		switcher = Gtk.StackSwitcher()
		switcher.set_stack(main)
		box.pack_start(switcher, True, True, 0)
		box.pack_start(main, True, True, 0)



win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
