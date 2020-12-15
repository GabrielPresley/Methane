import matplotlib
matplotlib.use('GTK3Agg')  # or 'GTK3Cairo'
import matplotlib.pyplot as plt
#
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#
fig = plt.figure()
ax = plt.axes(projection="3d")

manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox

# Example button
button = Gtk.Button(label='Click me')
button.show()
button.connect('clicked', lambda button: print('hi mom'))

# label = Gtk.Label()
# def update(event):
#     if event.xdata is None:
#         label.set_markup('Drag mouse over axes for position')
#     else:
#         label.set_markup(
#             f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')
#
# fig.canvas.mpl_connect('motion_notify_event', update)

plt.show()
