import tkinter

main = tkinter.Tk()

selection1 = tkinter.StringVar(main)
selection1.set("thing")

dropdown = tkinter.OptionMenu(main, selection1, "thing", "stuff", "doohicker")
dropdown.pack()

main.mainloop()

#test
