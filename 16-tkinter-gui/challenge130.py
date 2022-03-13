from tkinter import *
import csv

# create window
window = Tk()
window.title("Number CSV")
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

def saveToCsv():
    file = open("List130.csv", "w")
    tmp_list = num_list.get(0, END)
    for num in tmp_list:
        file.write(str(num) + "\n")
    file.close()

# create possibility for label, entry and button
info_message = Label(text="Enter number:")
info_message.place(x=10, y=100, width=90, height=25)
add_button = Button(text="Add number to list", command=addNumber)
add_button.place(x=100, y=150, width=300, height=25)
delete_button = Button(text="Reset list", command=clearList)
delete_button.place(x=100, y=200, width=300, height=25)
save_button = Button(text="Save list", command=saveToCsv)
save_button.place(x=100, y=250, width=300, height=25)

# execute
window.mainloop()