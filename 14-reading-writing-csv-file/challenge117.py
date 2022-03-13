import random

# initialize fields that will store variables later to be inserted into csv
score = 0
questions = []
answers = []
name = input("Enter your name: ")

# open file: if it exists already append, if it doesn't exist create new one
try:
    file = open("Quiz.csv", "x")
    file.write("Name,Question 1,Answer 1,Question 2,Answer 2,Score\n")
except FileExistsError:
    file = open("Quiz.csv", "a")

# do the math quiz
for i in range(0, 2):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(["+", "-", "*", "/"])
    correct = 0.0
    if op == "+":
        correct = num1 + num2
    elif op == "-":
        correct = num1 - num2
    elif op == "*":
        correct = num1 * num2
    else:
        correct = num1 / num2

    answer = float(input("The question is " + str(num1) + " " + op + " " + str(num2) + " please give your answer, rounded to two decimals: "))

    # check if user answer is correct
    if answer == round(correct, 2):
        score += 1

    # insert into list to later be inserted into csv
    questions.append(str(num1) + op + str(num2))
    answers.append(str(answer))

# insert into csv
doneQuiz = name + "," + questions[0] + "," + answers[0] + "," + questions[1] + "," + answers[1] + "," + str(score) + "\n"
file.write(doneQuiz)
file.close()