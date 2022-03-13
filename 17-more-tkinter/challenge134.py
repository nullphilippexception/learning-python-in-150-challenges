from tkinter import *
import random

# create window
window = Tk()
window.title("Math quiz")
window.geometry("500x500")

# Message that displays the question to user
left_box = Message(text="", width=25)
left_box.place(x=100, y=100, width=25, height=25)
right_box = Message(text="", width=25)
right_box.place(x=150, y=100, width=25, height=25)

# label that (visually) connects the number boxes and the answer
plus_sign = Label(text=" + ")
plus_sign.place(x=125, y=100, width=25, height=25)
equals_sign = Label(text=" = ")
equals_sign.place(x=175, y=100, width=25, height=25)

# entry box to enter user answer
answer_box = Entry()
answer_box.place(x=200, y=100, width=100, height=25)

# image that will be displayed as indicator for right or wrong answer
awaiting_answer = PhotoImage(file="waiting.gif")
right_answer = PhotoImage(file="right.gif")
wrong_answer = PhotoImage(file="wrong.gif")
answer_feedback = Label(window, image = awaiting_answer)
answer_feedback.image = awaiting_answer
answer_feedback.place(x=325, y=90, width=50, height=50)

# function that sets the question
def set_question():
    num1 = random.randint(10,50)
    num2 = random.randint(10,50)
    left_box["text"] = num1
    right_box["text"] = num2

# function that displays whether user answer was right or wrong
def submit_answer():
    num1 = int(left_box["text"])
    num2 = int(right_box["text"])
    user_answer = int(answer_box.get())
    if user_answer == (num1 + num2):
        answer_feedback.image = right_answer
        answer_feedback["image"] = right_answer
    else:
        answer_feedback.image = wrong_answer
        answer_feedback["image"] = wrong_answer
    answer_feedback.update()

# function that proceeds to next question
def next_question():
    answer_feedback.image = awaiting_answer
    answer_feedback["image"] = awaiting_answer
    answer_feedback.update()
    answer_box.delete(0, END)
    set_question()

# button that submits the entry
submit_button = Button(text="Submit answer", command=submit_answer)
submit_button.place(x=200, y=150, width=100, height=25)

# button that goes to next question
next_button = Button(text="Next question", command=next_question)
next_button.place(x=100, y=150, width=100, height=25)

#execute the function
def main():
    set_question()
    window.mainloop()

main()