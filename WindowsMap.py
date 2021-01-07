import tkinter

def readtime(string):
    item = ""
    lis = [] 
    string = list(string)
    
    for i in string:
        if(i == "\n"):
            return lis
        elif(i == ","):
            lis.append((int(item[0:2]) * 3600) + (int(item[3:5]) * 60) + int(item[6:]))
            item = ""
        elif(i == " "):
            pass
        else:
            item = item + i
    return lis 

canvas = 1

def redrawGraph():
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.gca(projection='3d')
    x = data[0]
    y = data[1]
    z = data[2]
    c = data[3]
    plot.scatter(x, y, z, c=c)
    plot.set_xlabel(selection[0].get())
    plot.set_ylabel (selection[1].get())
    plot.set_title(selection[1].get() + " vs. " + selection[0].get())
    
    global canvas
    
    if(canvas != 1):
        canvas.get_tk_widget().destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=main)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def readlist(string):
    item = ""
    lis = []
    string = list(string)
    
    for i in string:
        if(i == "\n"):
            return lis
        elif(i == ","):
            lis.append(float(item))
            item = ""

        elif(i == "["):
            pass
        else:
            item = item + i
    return lis

def loadData(slot, key):
    file = open("TransposedTestData.csv", "r")

    line = datamap[key]
    
    for i, content in enumerate(file):
        if(i == line):
            if(line == 3):
                data[slot] = readtime(content)
            else:
                data[slot] = readlist(content)
            
    file.close()
    
    

def updateGraph(event):
    
    
    loadData(0, event)
                    
    redrawGraph()
    
def updateGraph1(event):
    
    loadData(1, event)
                    
    redrawGraph()
    
def updateGraph2(event):
    
    loadData(2, event)
                    
    redrawGraph()
    
def updateGraph3(event):
    
    loadData(3, event)
                    
    redrawGraph()

main = tkinter.Tk()

updates  = [updateGraph, updateGraph1, updateGraph2, updateGraph3]

datamap = {"Pressure": 0, "Tempature": 1, "Humidity": 2, "Time": 3}

data[5][4]

dropdown = []
selection = []
for i in range(4):
    selection.append(tkinter.StringVar(main))
    selection[i].set("thing")
    
    dropdown.append(tkinter.OptionMenu(main, selection[i], "Pressure", "Tempature", "Humidity", "Time", command= updates[i]))
    dropdown[i].pack()
    
    loadData(i, "Pressure")

   # making a graph 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

redrawGraph()

main.mainloop()
