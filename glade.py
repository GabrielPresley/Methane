#!/usr/bin/python3
#
from gi.repository import Gtk
#
from matplotlib.figure import Figure
from numpy import sin, cos, pi, linspace
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar
#
myfirstwindow = Gtk.Window()
myfirstwindow.connect("delete-event", Gtk.main_quit)
myfirstwindow.set_default_size(100, 100) # these mean nothing to me as im on i3wm
myfirstwindow.set_title('Matplotlib')
#
box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
myfirstwindow.add(box)
#
#START matplotlib stuff


#END of Matplotlib stuff
canvas = FigureCanvas(fig)
box.pack_start(canvas, True, True, 0)
#
toolbar = NavigationToolbar(canvas, myfirstwindow)
box.pack_start(toolbar, False, True, 0)
#
myfirstwindow.show_all()
Gtk.main()
#
