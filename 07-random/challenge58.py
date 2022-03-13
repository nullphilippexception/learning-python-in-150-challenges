import random

score = 0

for i in range(0, 5):
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

    if answer == round(correct, 2):
        score += 1

print("You scored", score, "point(s)")
