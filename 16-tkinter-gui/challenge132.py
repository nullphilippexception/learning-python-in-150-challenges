from tkinter import *
import csv

# NOTE: this task is connected with challenge131, you need to run 131 first and create the CSV there
# before running this challenge

# create window
window = Tk()
window.title("Name and age CSV")
window.geometry("500x500")

# create input fields:
name_entry = Entry()
name_entry.place(x=100, y=100, width=300, height=25)
age_entry = Entry()
age_entry.place(x=100, y=150, width=300, height=25)

# function that saves to csv
def saveToCsv():
    file = open("List131.csv", "a")
    file.write(str(name_entry.get()) + "," + str(age_entry.get()) + "\n")
    file.close()

# function that displays the csv
def displayCsv():
    csv_display = Listbox()
    csv_display.place(x=100, y=300, width=300, height=100)
    file = open("List131.csv", "r")
    for row in file:
        csv_display.insert(csv_display.size(), row)
    file.close()

# labels for entry boxes
name_message = Label(text="Name:")
name_message.place(x=10, y=100, width=90, height=25)
age_message = Label(text="Age:")
age_message.place(x=10, y=150, width=90, height=25)

# buttons
save_button = Button(text="Add to CSV", command=saveToCsv)
save_button.place(x=100, y=200, width=300, height=25)
display_button = Button(text="Display CSV", command=displayCsv)
display_button.place(x=100, y=250, width=300, height=25)

# execute
window.mainloop()