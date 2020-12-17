#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-

""" Main application--embed Matplotlib figure in window with UI """

import gi
gi.require_version('Gtk', '3.0')

import numpy as np
from gi.repository import Gtk, GObject
from matplotlib.figure import Figure

# make sure cairocffi is installed, pycairo doesn't support FigureCanvasGTK3Agg
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg \
    as FigureCanvas

from matplotlib.patches import Ellipse
from typing import List, Tuple, Union
from math import sqrt


class Main(Gtk.Window):
    """ Main window UI """
    SIGMA = 10
    INVERT = -1

    def __init__(self) -> None:
        Gtk.Window.__init__(self, title='Gauss\' Circle Problem')
        self.connect('destroy', lambda _: Gtk.main_quit())
        self.set_border_width(10)
        self.set_default_size(650, 500)

        # Set up the l/r box layout
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # Set up the right column
        self.rcolumn = Gtk.VBox(spacing=0)
        self.rcolumn.set_spacing(10)
        self.box.pack_end(self.rcolumn, False, False, 20)

        # Set up spin button
        adjustment = Gtk.Adjustment(self.SIGMA, 1, 30, 1, 0, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        self.rcolumn.pack_start(self.spinbutton, False, False, 0)

        # Set up invert checkbox
        self.invertbutton = Gtk.CheckButton('Invert')
        self.invertbutton.set_active(True)
        self.invertbutton.connect('toggled', self.switch_toggle_parity, 'invert')
        self.rcolumn.add(self.invertbutton)

        # Set up update button
        self.update_plot_button = Gtk.Button(label='Update')
        self.update_plot_button.connect('clicked', self.update_sigma_event)
        self.rcolumn.add(self.update_plot_button)

        self.initial_plot()

    def calculate(self) -> None:
        """ Re-calculate using the formula """
        arr = np.zeros([self.SIGMA * 2 + 1] * 2)

        points = self.collect(int(self.SIGMA), int(self.SIGMA), self.SIGMA)

        # flip pixel value if it lies inside (or on) the circle
        for p in points:
            arr[p] = 1

        # plot ellipse on top of boxes to show their centroids lie inside
        circ = Ellipse(
            xy=(int(self.SIGMA), int(self.SIGMA)),
            width=2 * self.SIGMA,
            height=2 * self.SIGMA,
            angle=0.0
        )

        self.ax.clear()
        self.ax.add_artist(circ)
        circ.set_clip_box(self.ax.bbox)
        circ.set_alpha(0.2)
        circ.set_facecolor((1, 1, 1))
        self.ax.set_xlim(-0.5, 2 * self.SIGMA + 0.5)
        self.ax.set_ylim(-0.5, 2 * self.SIGMA + 0.5)

        # Plot the pixel centers
        self.ax.scatter(*zip(*points), marker='.',
            color='white' if self.INVERT == -1 else 'black')

        # now plot the array that's been created
        self.ax.imshow(self.INVERT * arr, interpolation='none', cmap='gray')

    def initial_plot(self) -> None:
        """ Set up the initial plot; only called once """
        self.fig = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.fig)
        self.box.pack_start(self.canvas, True, True, 0)
        self.ax = self.fig.add_subplot(111, aspect='equal')
        self.calculate()
        self.draw_plot()

    def update_sigma_event(self, button: Union[Gtk.Button, None] =None) -> None:
        """ Update sigma and trigger a replot """
        self.SIGMA = int(self.spinbutton.get_value())
        self.calculate()
        self.draw_plot()

    def switch_toggle_parity(self, button: Union[Gtk.CheckButton, None] =None,
            name: str ='') -> None:
        """ Switch the parity of the plot before update """
        self.INVERT *= -1

    def draw_plot(self) -> None:
        """ Draw or update the current plot """
        self.fig.canvas.draw()

    @staticmethod
    def collect(x: int, y: int, sigma: float =3.0) -> List[Tuple[int, int]]:
        """ create a small collection of points in a neighborhood of some
        point
        """
        neighborhood = []

        X = int(sigma)
        for i in range(-X, X + 1):
            Y = int(pow(sigma * sigma - i * i, 1/2))
            for j in range(-Y, Y + 1):
                neighborhood.append((x + i, y + j))

        return neighborhood


if __name__ == '__main__':
    window = Main()
    window.show_all()
    Gtk.main()
