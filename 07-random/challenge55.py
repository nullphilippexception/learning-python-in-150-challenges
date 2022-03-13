import random

rightNumber = random.randint(1, 5)
userNumber = int(input("Choose number between 1 and 5: "))

if userNumber == rightNumber:
    print("Well done")
else:
    hint = ""
    if userNumber > rightNumber:
        hint = "too high"
    else:  # must be too low than
        hint = "too low"
    userNumber = int(input("You are " + hint + " take another guess: "))

    if userNumber == rightNumber:
        print("Correct")
    else:
        print("You loose")
