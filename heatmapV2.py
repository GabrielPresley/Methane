#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
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
class ButtonWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="MMM Monitors Methane")
		self.set_border_width(10)


		"""
		class page: Creates a box to hold a stack or creates a label

		class stack: Creates a stack to hold grids

		class grid: Creates a grid to hold graphs and sliders

		def changex: Updates the scatter plot azimuth when a slider is moved

		def changey: Updates the scatter plot elevation when a slider is moved

		def changehist: Updates the histogram bins when a slider is moved

		class plot3d: Creates a scatter plot and adds it to a canvas

		class histogram: Creates a histogram and adds it to a canvas

		class boxplot: Creates a boxplot and adds it to a canvas

		if (plottype = "scatter"): Creates a grid to hold a scatter plot and 2 sliders

		if (plottype = "histogram"): Creates a grid to hold a histogram and 1 slider

		if (plottype = "box"): Creates a grid to hold a boxplot
		"""

		class page:
			def __init__(self, time=[], lat=[], lon=[], alt=[], data=[], name="", text=""):
				class stack:
					def __init__(self, time, lat, lon, alt, data, name):
						class grid:

							# Updates scatter plot azimuth when slider is moved
							def changex(self, slide, grid, ax, fig, column, row):
								grid.remove(fig)
								ax.view_init(elev=ax.elev, azim=slide.get_value())
								grid.attach(fig, column, row, 1, 1)

							# Updates scatter plot elevation when slider is moved
							def changey(self, slide, grid, ax, fig, column, row):
								grid.remove(fig)
								ax.view_init(elev=90 - slide.get_value(), azim=ax.azim)
								grid.attach(fig, column, row, 1, 1)

							# Updates histogram bins when slider is moved
							def changehist(self, slide, grid, ax, fig, data, name, column, row):
								grid.remove(fig)
								ax.cla()
								ax.hist(data, bins=int(slide.get_value()))
								ax.set_title("%s" %name)
								grid.attach(fig, column, row, 1, 1)
								grid.show_all()

							def __init__(self, plottype, time, lat, lon, alt, data, name):

								# Create a scatter plot graph
								class plot3d:
									def __init__(self, lat, lon, alt, data, name):
										fig = Figure()
										self.ax = fig.gca(projection='3d')
										self.ax.scatter(latitude, longitude, altitude, c=data, s=1)
										self.ax.set_title("%s Heatmap" %name)
										self.ax.set_xlabel("x (m)")
										self.ax.set_ylabel("y (m)")
										self.ax.set_zlabel("altitude (m)")
										self.ax.view_init(30, 45)

										self.canvas = FigureCanvas(fig)
										self.canvas.set_size_request(800, 800)

								# Create a histogram graph
								class histogram:
									def __init__(self, data, name):
										fig = Figure()
										self.ax = fig.gca()
										self.ax.hist(data, bins=75)
										self.ax.set_title("%s" %name)

										self.canvas = FigureCanvas(fig)
										self.canvas.set_size_request(800, 800)

								# Create a boxplot graph
								class boxplot:
									def __init__(self, data, name):
										fig = Figure()
										self.ax = fig.gca()
										self.ax.boxplot(data)
										self.ax.set_title("%s" %name)

										self.canvas = FigureCanvas(fig)
										self.canvas.set_size_request(800, 800)

								class plot2d:
									def __init__(self, time, data, name):
										fig = Figure()
										self.ax = fig.gca()
										self.plot(data)
										self.ax.set_title("%s vs. Time" %name)
										self.ax.set_xlabel("Time (s)")
										self.ax.set_ylabel(name)

								self.grid = Gtk.Grid()
								self.grid.set_row_spacing(5)
								self.grid.set_column_spacing(5)

								# Create a scatter plot grid
								if (plottype == "scatter"):
									slide1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=Gtk.Adjustment(45, 0, 360, 5, 10, 0))
									slide2 = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=Gtk.Adjustment(30, 0, 90, 5, 10, 0))

									plot = plot3d(lat, lon, alt, data, name)

									self.grid.attach(plot.canvas, 1, 1, 1, 1)
									self.grid.attach(slide1, 1, 0, 1, 1)
									self.grid.attach(slide2, 0, 1, 1, 1)

									slide1.connect("value-changed", self.changex, self.grid, plot.ax, plot.canvas, 1, 1)
									slide2.connect("value-changed", self.changey, self.grid, plot.ax, plot.canvas, 1, 1)

								# Create a histogram grid
								elif (plottype == "histogram"):
									slide = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=Gtk.Adjustment(75, 0, 100, 5, 10, 0))

									plot = histogram(data, name)

									self.grid.attach(plot.canvas, 0, 1, 1, 1)
									self.grid.attach(slide, 0, 0, 1, 1)

									slide.connect("value-changed", self.changehist, self.grid, plot.ax, plot.canvas, data, name, 0, 1)

								# Create a boxplot grid
								elif (plottype == "box"):
									plot = boxplot(data, name)

									self.grid.attach(plot.canvas, 0, 0, 1, 1)

								elif (plottype == "2d"):
									plot = plot2d(time, data, name)

									self.grid.attach(plot.canvas, 0, 0, 1, 1)

						# Stack
						self.stack = Gtk.Stack()
						self.switch = Gtk.StackSwitcher()

						grid1 = grid("scatter", time, lat, lon, alt, data, name)
						grid2 = grid("histogram", time, lat, lon, alt, data, name)
						grid3 = grid("box", time, lat, lon, alt, data, name)
						grid4 = grid("time", time, lat, lon, alt, data, name)

						self.stack.add_titled(grid1.grid, "3d", "3D Plot")
						self.stack.add_titled(grid2.grid, "hist", "Histogram")
						self.stack.add_titled(grid3.grid, "box", "Box Plot")
						self.stack.add_titled(grid4.grid, "2d", "2D Plot")

						self.switch.set_stack(self.stack)

				# Page
				self.graph = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

				self.stack = stack(lat, lon, alt, data, name)

				self.graph.pack_start(self.stack.switch, True, True, 0)
				self.graph.pack_start(self.stack.stack, True, True, 0)

				self.label = Gtk.Label(report)
				self.label.set_alignment(0, 0)

		# Open files
		text = open("Data/Report.txt", "r")
		report = text.read()

		results = []
		with open("Data/transposedcardata.csv") as csvfile:
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
		time = results[7][2:]

		# Create pages and add them to notebook
		notebook = Gtk.Notebook()

		page1 = page(time, latitude, longitude, altitude, methane, "Methane")
		page2 = page(time, latitude, longitude, altitude, humidity, "Humidity")
		page3 = page(time, latitude, longitude, altitude, temperature, "Temperature")
		page4 = page(time, latitude, longitude, altitude, pressure, "Pressure")
		page5 = page(text=report)

		notebook.append_page(page1.graph, Gtk.Label("Methane"))
		notebook.append_page(page2.graph, Gtk.Label("Humidity"))
		notebook.append_page(page3.graph, Gtk.Label("Temperature"))
		notebook.append_page(page4.graph, Gtk.Label("Pressure"))
		notebook.append_page(page5.label, Gtk.Label("Report"))

		self.add(notebook)

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
