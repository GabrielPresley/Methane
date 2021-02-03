#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
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
		Gtk.Window.__init__(self, title="MMM Monitors Methane")
		self.set_border_width(10)

		grid1 = Gtk.Grid()
		grid2 = Gtk.Grid()
		grid3 = Gtk.Grid()
		grid4 = Gtk.Grid()

		grid1.set_row_spacing(5)
		grid1.set_column_spacing(5)
		grid2.set_row_spacing(5)
		grid2.set_column_spacing(5)
		grid3.set_row_spacing(5)
		grid3.set_column_spacing(5)
		grid4.set_row_spacing(5)
		grid4.set_column_spacing(5)

		txt = open("Data/Report.txt", "r")

		report = Gtk.Label(txt.read())
		report.set_alignment(0, 0)

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
		latmin = latitude.min()
		latmax = latitude.max()
		lonmin = longitude.min()
		lonmax = longitude.max()

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
		ax1.view_init(30, 45)

		ax2.scatter(latitude, longitude, altitude, c=humidity, s=1)
		ax2.set_xlim3d(x1, x2)
		ax2.set_ylim3d(y1, y2)
		ax2.set_title("Humidity Heatmap")
		ax2.set_xlabel("x (m)")
		ax2.set_ylabel("y (m)")
		ax2.set_zlabel("altitude (m)")
		ax2.view_init(30, 45)

		ax3.scatter(latitude, longitude, altitude, c=temperature, s=1)
		ax3.set_xlim3d(x1, x2)
		ax3.set_ylim3d(y1, y2)
		ax3.set_title("Temperature Heatmap")
		ax3.set_xlabel("x (m)")
		ax3.set_ylabel("y (m)")
		ax3.set_zlabel("altitude (m)")
		ax3.view_init(30, 45)

		ax4.scatter(latitude, longitude, altitude, c=pressure, s=1)
		ax4.set_xlim3d(x1, x2)
		ax4.set_ylim3d(y1, y2)
		ax4.set_title("Pressure Heatmap")
		ax4.set_xlabel("x (m)")
		ax4.set_ylabel("y (m)")
		ax4.set_zlabel("altitude (m)")
		ax4.view_init(30, 45)

		#Create notebook
		notebook = Gtk.Notebook()
		page1 = Gtk.Grid()
		page2 = Gtk.Grid()
		page3 = Gtk.Grid()
		page4 = Gtk.Grid()
		page5 = Gtk.Grid()

		#Create canvases
		met = FigureCanvas(fig1)
		hum = FigureCanvas(fig2)
		tem = FigureCanvas(fig3)
		pre = FigureCanvas(fig4)

		met.set_size_request(800, 800)
		hum.set_size_request(800, 800)
		tem.set_size_request(800, 800)
		pre.set_size_request(800, 800)

		#Sliders
		mad1 = Gtk.Adjustment(45, 0, 360, 5, 10, 0)
		mad2 = Gtk.Adjustment(60, 0, 90, 5, 10, 0)
		had1 = Gtk.Adjustment(45, 0, 360, 5, 10, 0)
		had2 = Gtk.Adjustment(60, 0, 90, 5, 10, 0)
		tad1 = Gtk.Adjustment(45, 0, 360, 5, 10, 0)
		tad2 = Gtk.Adjustment(60, 0, 90, 5, 10, 0)
		pad1 = Gtk.Adjustment(45, 0, 360, 5, 10, 0)
		pad2 = Gtk.Adjustment(60, 0, 90, 5, 10, 0)

		mslide1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=mad1)
		mslide2 = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=mad2)
		hslide1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=had1)
		hslide2 = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=had2)
		tslide1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=tad1)
		tslide2 = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=tad2)
		pslide1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=pad1)
		pslide2 = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=pad2)

		mslide1.connect("value-changed", self.changex, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		mslide2.connect("value-changed", self.changey, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		hslide1.connect("value-changed", self.changex, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		hslide2.connect("value-changed", self.changey, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		tslide1.connect("value-changed", self.changex, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		tslide2.connect("value-changed", self.changey, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		pslide1.connect("value-changed", self.changex, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)
		pslide2.connect("value-changed", self.changey, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4)

		#Add everything to display
		grid1.attach(mslide1, 1, 0, 1, 1)
		grid1.attach(mslide2, 0, 1, 1, 1)
		grid2.attach(hslide1, 1, 0, 1, 1)
		grid2.attach(hslide2, 0, 1, 1, 1)
		grid3.attach(tslide1, 1, 0, 1, 1)
		grid3.attach(tslide2, 0, 1, 1, 1)
		grid4.attach(pslide1, 1, 0, 1, 1)
		grid4.attach(pslide2, 0, 1, 1, 1)
		grid1.attach(met, 1, 1, 1, 1)
		grid2.attach(hum, 1, 1, 1, 1)
		grid3.attach(tem, 1, 1, 1, 1)
		grid4.attach(pre, 1, 1, 1, 1)

		notebook.append_page(grid1, Gtk.Label("Methane"))
		notebook.append_page(grid2, Gtk.Label("Humidity"))
		notebook.append_page(grid3, Gtk.Label("Temperature"))
		notebook.append_page(grid4, Gtk.Label("Pressure"))
		notebook.append_page(report, Gtk.Label("Report"))
		self.add(notebook)

		#Update azimuth
	def changex(self, slider, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4):
		if (notebook.get_current_page() == 0):
			grid1.remove(met)
			ax1.view_init(elev=ax1.elev, azim=slider.get_value())
			grid1.attach(met, 1, 1, 1, 1)
		elif (notebook.get_current_page() == 1):
			grid2.remove(hum)
			ax2.view_init(elev=ax2.elev, azim=slider.get_value())
			grid2.attach(hum, 1, 1, 1, 1)
		elif (notebook.get_current_page() == 2):
			grid3.remove(tem)
			ax3.view_init(elev=ax3.elev, azim=slider.get_value())
			grid3.attach(tem, 1, 1, 1, 1)
		else:
			grid4.remove(pre)
			ax4.view_init(elev=ax4.elev, azim=slider.get_value())
			grid4.attach(pre, 1, 1, 1, 1)
		notebook.show_all()

		#Update elevation
	def changey(self, slider, notebook, grid1, grid2, grid3, grid4, met, hum, tem, pre, ax1, ax2, ax3, ax4):
		if (notebook.get_current_page() == 0):
			grid1.remove(met)
			ax1.view_init(azim=ax1.azim, elev=90 - slider.get_value())
			grid1.attach(met, 1, 1, 1, 1)
		elif (notebook.get_current_page() == 1):
			grid2.remove(hum)
			ax2.view_init(azim=ax2.azim, elev=90 - slider.get_value())
			grid2.attach(hum, 1, 1, 1, 1)
		elif (notebook.get_current_page() == 2):
			grid3.remove(tem)
			ax3.view_init(azim=ax3.azim, elev=90 - slider.get_value())
			grid3.attach(tem, 1, 1, 1, 1)
		else:
			grid4.remove(pre)
			ax4.view_init(azim=ax4.azim, elev=90 - slider.get_value())
			grid4.attach(pre, 1, 1, 1, 1)
		notebook.show_all()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
