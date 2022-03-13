from tkinter import *

# create window
window = Tk()
window.title("Enter Name")
window.geometry("500x500")

# create messagebox that will later display greeting
greeting_display = Message(text="")
greeting_display.place(x=100, y=200, width=300, height=50)

# define function that will display name
def displayName():
    greetingText = "Hello " + name_entry.get()
    greeting_display["text"] = greetingText
    greeting_display["bg"] = "blue"
    greeting_display["fg"] = "white"

# create possibility for label, entry and button
info_message = Label(text="Enter name:")
info_message.place(x=10, y=100, width=90, height=25)
name_entry = Entry(text=0)
name_entry.place(x=100, y=100, width=300, height=25)
entry_button = Button(text="Click here", command=displayName)
entry_button.place(x=100, y=150, width=300, height=25)

# execute
window.mainloop()