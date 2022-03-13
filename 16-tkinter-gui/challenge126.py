from tkinter import *

# set up basic program structure
window = Tk()
window.title("Sum number")
window.geometry("500x500")

# entry box
number_entry = Entry(text="enter a number")
number_entry.place(x=100, y=40, width=300, height=50)

# create messagebox that will later display greeting
number_display = Message(text="0")
number_display.place(x=100, y=200, width=300, height=50)

# function that refreshes displayed number
def add_sum():
    displayed_number = int(number_entry.get()) + int(number_display["text"])
    number_display["text"] = displayed_number

# function that sets displayed number to zero
def set_zero():
    number_display["text"] = 0

# buttons
sum_button = Button(text="Add to sum", command=add_sum)
sum_button.place(x=100, y=90, width=300, height=50)
reset_button = Button(text="Reset to 0", command=set_zero)
reset_button.place(x=100, y=140, width=300, height=50)

window.mainloop()

