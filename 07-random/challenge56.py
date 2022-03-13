import random

randomNumber = random.randint(1,10)
userNumber = int(input("Guess number: "))

while userNumber != randomNumber:
    userNumber = int(input("Guess again: "))
    
print("Your guessed the right number")