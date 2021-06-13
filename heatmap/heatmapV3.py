#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
#
from os import listdir
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
import os
#
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
"""
1 Notebook
5 boxes
1 stack, 1 header(1 switch, 1 dropdown)
4 grids

notebook[box].stack[grid]
notebook[box].header.switch
notebook[box].header.dropdown
"""


class ButtonWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="MMM Monitors Methane")

		# Updates histogram bins when slider is moved
		def changehist(slide, grid, ax, fig, data, name):
			grid.remove(fig)
			ax.cla()
			ax.hist(data, bins=int(slide.get_value()))
			ax.set_title(name)
			grid.attach(fig, 0, 1, 1, 1)
			grid.show_all()

		def changedropdown(dropdown, results, page, grid, canvas, ax):
			grid[4*page].remove(canvas[4*page])
			grid[4*page+1].remove(canvas[4*page+1])
			grid[4*page+2].remove(canvas[4*page+2])
			grid[4*page+3].remove(canvas[4*page+3])

			results.clear()
			try:
				with open(f"../Data/{dropdown.get_active_text()}") as csvfile:
					reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
					try:
						for row in reader:
							results.append(row)

					except ValueError:
						print("Data file has not been cleaned or is not valid\nPlease choose a valid file")
						results.clear()
						for i in range(9):
							results.append([1])

						#print(len(results[5]),len(results[6]),len(results[4]),len(results[0]),len(results[0]))
					ax[4*page].cla()
					ax[4*page+1].cla()
					ax[4*page+2].cla()
					ax[4*page+3].cla()
					ax[4*page].scatter(results[5], results[6], results[4], c=results[0], s=1)
					ax[4*page+1].hist(results[page], bins=75)
					ax[4*page+2].boxplot(results[page])
					ax[4*page+3].plot(results[7], results[page])

			except FileNotFoundError:
				pass # basically hide the errors when "please choose text file is up"

			grid[4*page+0].attach(canvas[4*page+0], 1, 1, 1, 1)
			grid[4*page+1].attach(canvas[4*page+1], 0, 1, 1, 1)
			grid[4*page+2].attach(canvas[4*page+2], 0, 0, 1, 1)
			grid[4*page+3].attach(canvas[4*page+3], 0, 0, 1, 1)
			#print(dropdown.get_active_text())


		# Initialization
		notebook = []
		header = []
		stack = []
		switch = []
		dropdown = []
		grid = []
		fig = []
		ax = []
		canvas = []
		notebook1 = Gtk.Notebook()

		for i in range(4):
			notebook.append(Gtk.Box(orientation=Gtk.Orientation.VERTICAL))
			header.append(Gtk.Box())
			stack.append(Gtk.Stack())
			switch.append(Gtk.StackSwitcher())
			dropdown.append(Gtk.ComboBoxText())
			for j in range(4):
				grid.append(Gtk.Grid())
				fig.append(Figure())
				if (i == 0):
					ax.append(fig[i].gca(projection='3d'))
				else:
					ax.append(fig[i].gca())
				canvas.append(FigureCanvas(fig[i]))

		results = []

		# Dropdown
		for i in range(len(dropdown)):
			dropdown[i].append_text("Please Select A File")
			for data in os.listdir("../Data/"):
				if data.endswith(".csv"):
					dropdown[i].append_text(data)
			dropdown[i].set_active(0)
			dropdown[i].connect("changed", changedropdown, results, i, grid, canvas, ax)
		if dropdown[0].get_active_text() != "Please Select A File":
			with open(f"../Data/{dropdown[0].get_active_text()}") as csvfile:
				reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
				for row in reader: # each row is a list
					results.append(row)
		else:
			for i in range(9):
				results.append([1])

		# Grid
		for i, name, data in zip(range(int(len(grid) / len(stack))), ["Methane", "Humidity", "Temerature", "Pressure"], [results[0], results[1], results[2], results[3]]):
			for j, name2 in zip(range(int(len(grid) / len(stack))), ["Heatmap", "Histogram", "Box Plot", "2D Graph"]):
				if (j == 0):
					ax[4*i+j] = fig[4*i+j].gca(projection='3d')
					ax[4*i+j].scatter(results[5], results[6], results[4], c=data, s=1)
					ax[4*i+j].set_title(name)
					ax[4*i+j].set_xlabel("x (m)")
					ax[4*i+j].set_ylabel("y (m)")
					ax[4*i+j].set_zlabel("altitude (m)")
					ax[4*i+j].view_init(30, 45)

					canvas[4*i+j] = FigureCanvas(fig[4*i+j])
					canvas[4*i+j].set_size_request(800, 800)

					grid[4*i+j].attach(canvas[4*i+j], 0, 0, 1, 1)

				if (j == 1):
					ax[4*i+j] = fig[4*i+j].gca()
					ax[4*i+j].hist(data, bins=75)
					ax[4*i+j].set_title(name)

					canvas[4*i+j] = FigureCanvas(fig[4*i+j])
					canvas[4*i+j].set_size_request(800, 800)

					slider = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=Gtk.Adjustment(75, 0, 100, 5, 10, 0))

					grid[4*i+j].attach(canvas[4*i+j], 0, 1, 1, 1)
					grid[4*i+j].attach(slider, 0, 0, 1, 1)

					slider.connect("value-changed", changehist, grid[4*i+j], ax[4*i+j], canvas[4*i+j], data, name)

				if (j == 2):
					ax[4*i+j] = fig[4*i+j].gca()
					ax[4*i+j].boxplot(data)
					ax[4*i+j].set_title(name)

					canvas[4*i+j] = FigureCanvas(fig[4*i+j])
					canvas[4*i+j].set_size_request(800, 800)

					grid[4*i+j].attach(canvas[4*i+j], 0, 0, 1, 1)

				if (j == 3):
					ax[4*i+j] = fig[4*i+j].gca()
					ax[4*i+j].plot(results[7], data)
					ax[4*i+j].set_title(f"{name} vs. Time")
					ax[4*i+j].set_xlabel("Time (s)")
					ax[4*i+j].set_ylabel(name)

					canvas[4*i+j] = FigureCanvas(fig[4*i+j])
					canvas[4*i+j].set_size_request(800, 800)

					grid[4*i+j].attach(canvas[4*i+j], 0, 0, 1, 1)

				stack[i].add_titled(grid[4*i+j], f"{name2, i}", name2)

		# Header
			header[i].pack_start(switch[i], True, True, 0)
			header[i].pack_end(dropdown[i], True, True, 0)
			switch[i].set_stack(stack[i])

			notebook[i].pack_start(header[i], True, True, 0)
			notebook[i].pack_start(stack[i], True, True, 0)
			notebook1.append_page(notebook[i], Gtk.Label(label=name))

		text = open("../Data/Report.txt", "r")
		report = text.read()
		reportlabel = Gtk.Label(report)
		reportlabel.set_alignment(0, 0)

		notebook.append(reportlabel)
		notebook1.append_page(notebook[-1], Gtk.Label(label="Report"))

		self.add(notebook1)


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
