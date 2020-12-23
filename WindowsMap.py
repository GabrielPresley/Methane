import tkinter

main = tkinter.Tk()

selection1 = tkinter.StringVar(main)
selection.value = "thing"

dropdown = tkinter.OptionMenu(main, selection1, "stuff")
dropdown.pack()

main.mainloop()