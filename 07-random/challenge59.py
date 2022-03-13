import random

randColor = random.choice(["blue", "green", "red", "yellow", "orange"])
userColor = input("Choose a color: ")

while randColor != userColor.lower():
    if randColor == "blue":
        userColor = input("You are probably feeling BLUE right now, guess again: ")
    elif randColor == "green":
        userColor = input("I bet you are GREEN with envy, guess again: ")
    elif randColor == "red":
        userColor = input("You are probably seeing RED right now, guess again: ")
    elif randColor == "yellow":
        userColor = input("You are so close to the YELLOW part of the egg, guess again: ")
    else:  # must be orange in this case
        userColor = input("You are as smart as an ORANGE, guess again: ")

print("Well done")
