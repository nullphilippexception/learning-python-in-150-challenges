from tkinter import *

# create window
window = Tk()
window.title("Greeting")
window.geometry("500x500")
# window.wm_iconbitmap(“... .ico”)
window.configure(background="black")

# place my logo
logo = PhotoImage(file="logo.gif")
logo_display = Label(image=logo)
logo_display.place(x=150, y=100, width=200, height=150)

# output box
message_box = Message(text="", anchor="w", width=200) # learning: message needs two widths!
message_box.place(x=200, y=350, width=200, height=25)

# name entry label and entry box
entry_label = Label(text="Name: ")
entry_label.place(x=100, y=300, width=100, height=25)
entry_box = Entry()
entry_box.place(x=200, y=300, width=200, height=25)

# function that will display greeting
def displayGreeting():
    name = entry_box.get()
    message_box["text"] = "Hello " + name

# button
display_button = Button(text="Press me", command=displayGreeting)
display_button.place(x=100, y=350, width=100, height=25)

# exectue
window.mainloop()