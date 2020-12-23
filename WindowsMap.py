import tkinter

main = tkinter.Tk()

selection1 = tkinter.StringVar(main)
selection1.set("thing")

dropdown = []
for i in range(4):
    dropdown.append(tkinter.OptionMenu(main, selection1, "thing", "stuff", "doohicker"))
    dropdown[i].pack()

main.mainloop()

#test
