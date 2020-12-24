"""import tkinter

main = tkinter.Tk()

selection[i] = tkinter.StringVar(main)
selection[i].set("thing")

dropdown = []
for i in range(4):
    dropdown.append(tkinter.OptionMenu(main, selection[i], "thing", "stuff", "doohicker"))
    dropdown[i].pack()

main.mainloop()"""


import tkinter

main = tkinter.Tk()



dropdown = []
selection = []
for i in range(4):
	selection.append(tkinter.StringVar(main))
	selection[i].set("thing")
	
	dropdown.append(tkinter.OptionMenu(main, selection[i], "thing", "stuff", "doohicker"))
	dropdown[i].pack()

main.mainloop()
