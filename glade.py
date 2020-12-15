#!/usr/bin/python3

from gi.repository import Gtk

from matplotlib.figure import Figure
from numpy import sin, cos, pi, linspace
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar

myfirstwindow = Gtk.Window()
myfirstwindow.connect("delete-event", Gtk.main_quit)
myfirstwindow.set_default_size(500, 500)
myfirstwindow.set_title('Matplotlib')

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
myfirstwindow.add(box)

fig = Figure(figsize=(5,5), dpi=80) # set plot size
ax = fig.add_subplot(111)
#Start matplotlib




ax = fig.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

fig.tight_layout()

canvas = FigureCanvas(fig)
box.pack_start(canvas, True, True, 0)

toolbar = NavigationToolbar(canvas, myfirstwindow)
box.pack_start(toolbar, False, True, 0)

myfirstwindow.show_all()
Gtk.main()
