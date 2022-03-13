from tkinter import *

# set up basic program structure
window = Tk()
window.title("Background color")
window.geometry("500x500")

# create drop down list
color = StringVar(window)
color.set("Pick a color")
colorList = OptionMenu(window,color,"blue", "yellow", "red", "green")
colorList.place(x=200, y=200, width=100, height=50)

# function that changes color
def changeColor():
    if color.get() != "Pick a color":
        window.configure(background=color.get())

# button that activates function
activate_button = Button(text="Click me", command=changeColor)
activate_button.place(x=200, y=300, width=100, height=50)

# execute
window.mainloop()