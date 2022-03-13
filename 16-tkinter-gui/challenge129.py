from tkinter import *

# create window
window = Tk()
window.title("Number list")
window.geometry("500x500")

# create box where number will be placed
number_entry = Entry(text=0)
number_entry.place(x=100, y=100, width=300, height=25)

# list of numbers
num_list = Listbox()
num_list.place(x=100, y=300, width=300, height=50)

def addNumber():
    num = number_entry.get()
    if num.isdigit():
        num_list.insert(num_list.size(), num)
    else:
        number_entry.delete(0, END)

def clearList():
    num_list.delete(0, END)

# create possibility for label, entry and button
info_message = Label(text="Enter number:")
info_message.place(x=10, y=100, width=90, height=25)
add_button = Button(text="Add number to list", command=addNumber)
add_button.place(x=100, y=150, width=300, height=25)
delete_button = Button(text="Reset list", command=clearList)
delete_button.place(x=100, y=200, width=300, height=25)

# execute
window.mainloop()