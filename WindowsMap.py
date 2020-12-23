import tkinter

main = tkinter.Tk()

selection1 = StringVar(main)

dropdown = tkinter.OptionMenu(main, selection1, "stuff")
dropdown.pack()

main.mainloop()