from tkinter import *

# create window
window = Tk()
window.title("miles and km converter")
window.geometry("500x500")

# create box where number will be placed
number_entry = Entry(text=0)
number_entry.place(x=100, y=100, width=300, height=25)

# create messagebox that will later display result
result_display = Message(text="")
result_display.place(x=100, y=250, width=300, height=50)

# define functions
def miles_to_km():
    num = float(number_entry.get())*1.6093
    result_display["text"] = num

def km_to_miles():
    num = float(number_entry.get())*0.6214
    result_display["text"] = num

# create possibility for label, entry and button
info_message = Label(text="Enter number:")
info_message.place(x=10, y=100, width=90, height=25)
km_to_miles_button = Button(text="km to miles", command=km_to_miles)
km_to_miles_button.place(x=100, y=150, width=300, height=25)
miles_to_km_button = Button(text="miles to km", command=miles_to_km)
miles_to_km_button.place(x=100, y=200, width=300, height=25)

# execute
window.mainloop()