import random

computerChoice = random.choice(["heads", "tails"])
playerChoice = input("Make your coin flip choice (heads/tails): ")

if computerChoice == playerChoice.lower() :
    print("You win")
else :
    print("Bad luck")

print("The computer chose", computerChoice)