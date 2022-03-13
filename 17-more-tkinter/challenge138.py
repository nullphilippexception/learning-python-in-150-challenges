from tkinter import *

# set up basic program structure
window = Tk()
window.title("Number images")
window.geometry("500x500")

# image that will be displayed when number is entered
zero = PhotoImage(file="0.gif")
current_display = Label(window, image = zero)
current_display.image = zero
current_display.place(x=200, y=300, width=100, height=100)

# label that instructs user
instruct_user = Label(text="Enter a number: ")
instruct_user.place(x=100, y=100, width=100, height=50)

# entry box where user can enter number
num_entry = Entry()
num_entry.place(x=200, y=100, width=100, height=50)

# function that displays the chosen number
def displayNumber():
    chosen_num_file = num_entry.get() + ".gif"
    num_image = PhotoImage(file=chosen_num_file)
    current_display.image = num_image
    current_display["image"] = num_image
    current_display.update()

# button that triggers function to display number
display_button = Button(text="Display number", command=displayNumber)
display_button.place(x=300, y=100, width=100, height=50)

# execute
window.mainloop()