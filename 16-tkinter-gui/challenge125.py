from tkinter import *
import random

# create window
window = Tk()
window.title("Dice Roll")
window.geometry("500x500")

# create messagebox that will later display greeting
dice_display = Message(text="")
dice_display.place(x=100, y=200, width=300, height=50)

# define function that simulates dice
def diceRoll():
    diceResult = random.randint(1,6)
    dice_display["text"] = diceResult

# define button that enables diceroll
dice_button = Button(text="Click for diceroll", command=diceRoll)
dice_button.place(x=100, y=100, width=300, height=50)

window.mainloop()

