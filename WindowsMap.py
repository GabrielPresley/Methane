import tkinter

def readtime(string):
    item = ""
    lis = [] 
    string = list(string)
    
    for i in string:
        if(i == "\n"):
            return lis
        elif(i == ","):
            print(item)
            lis.append((int(item[0:2]) * 3600) + (int(item[3:5]) * 60) + int(item[6:]))
            item = ""
        elif(i == " "):
            pass
        else:
            item = item + i
    return lis

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
    print(data)
    loadData(0, event)
    print("works")

main = tkinter.Tk()

datamap = {"Pressure": 0, "Tempature": 1, "Humidity": 2, "Time": 3}

data = [[1, 2, 3, 4, 5],
        [1, 3, 2, 5, 4],
        [5, 4, 3, 2, 1], 
        [3, 4, 5, 1, 2]]

dropdown = []
selection = []
for i in range(4):
    selection.append(tkinter.StringVar(main))
    selection[i].set("thing")
    
    dropdown.append(tkinter.OptionMenu(main, selection[i], "Pressure", "Tempature", "Humidity", "Time", command = updateGraph))
    dropdown[i].pack()

main.mainloop()

# making a graph 

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
plot = fig.add_subplot(111)
plot.plot(t, 2 * np.sin(2 * np.pi * t))
plot.set_xlabel('X Axis')
plot.set_ylabel ('Y Axis')
set_title('Title')
                 

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


