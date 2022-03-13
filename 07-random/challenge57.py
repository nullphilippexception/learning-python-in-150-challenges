import random

randomNumber = random.randint(1, 10)
userNumber = int(input("Guess number: "))

while userNumber != randomNumber:
    hint = "Too high" #  default, check if hint should be too low
    if userNumber < randomNumber:
        hint = "Too low"
    userNumber = int(input(hint + ", guess again: "))

print("Your guessed the right number")