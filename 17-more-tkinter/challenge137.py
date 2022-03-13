from tkinter import *

# set up basic program structure
window = Tk()
window.title("Name & Gender list")
window.geometry("500x500")

# create text file
file = open("challenge137.txt", "w")
file.close()

# create entry box and info labels
name_entry = Entry()
name_entry.place(x=200, y=100, width=150, height=50)
name_info = Label(text="Enter name:")
name_info.place(x=100, y=100, width=100, height=50)
gender_info = Label(text="Pick gender:")
gender_info.place(x=100, y=200, width=100, height=50)

# create drop down list
gender = StringVar(window)
gender.set("Pick a gender")
genderList = OptionMenu(window,gender,"male", "female", "other/no answer")
genderList.place(x=200, y=200, width=150, height=50)

# create listbox
entries = Listbox()
entries.place(x=200, y=400, width=150, height=50)

# function that puts data into list
def createEntry():
    new_name = name_entry.get()
    new_gender = gender.get()
    new_entry = new_name + ", " + new_gender
    entries.insert(entries.size(), new_entry)
    edit_file = open("challenge137.txt", "a")
    new_entry += "\n"
    edit_file.write(new_entry)
    edit_file.close()

# function to display txt file in shell
def displayShell():
    display_file = open("challenge137.txt", "r")
    for line in display_file:
        print(line)
    display_file.close()

# button that activates function
activate_button = Button(text="Click me", command=createEntry)
activate_button.place(x=200, y=300, width=150, height=50)

# button that displays txt in shell
activate_button = Button(text="Display in shell", command=displayShell)
activate_button.place(x=300, y=300, width=150, height=50)

# execute
window.mainloop()