from tkinter import *

# create window
window = Tk()
window.title("Enter Name")
window.geometry("500x500")

# lsit of names
name_list = Listbox()
name_list.place(x=100, y=300, width=300, height=50)

# define function that will display name
def addNameToList():
    currentName = name_entry.get()
    name_list.insert(name_list.size(), currentName)

# define function to reset list
def resetList():
    name_list.delete(0, name_list.size()-1)

# create possibility for label, entry and button
info_message = Label(text="Enter name:")
info_message.place(x=10, y=100, width=90, height=25)
name_entry = Entry(text=0)
name_entry.place(x=100, y=100, width=300, height=25)
entry_button = Button(text="Insert name", command=addNameToList)
entry_button.place(x=100, y=150, width=300, height=25)
delete_button = Button(text="Delete names", command=resetList)
delete_button.place(x=100, y=250, width=300, height=25)

# execute
window.mainloop()