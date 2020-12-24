import tkinter

def readlist(string):
    item = ""
    lis = []
    string = list(string)
    
    for i in string:
        if(i == "\n"):
            return lis
        elif(i == ","):
            lis.append(float(item))
        elif(i == "["):
            pass
        else:
            item = item + i

def loadData(slot, key):
    file = open("TransposedTestData.csv", "r")

    line = datamap[key]
    
    for i, content in enumerate(file):
        if(i == line):
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
