import tkinter

def updateGraph(event):
    #will update the graph when the event is called. to be edited later
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
