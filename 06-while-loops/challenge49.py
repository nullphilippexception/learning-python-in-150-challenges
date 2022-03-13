compnum = 50
number = int(input("Enter number: "))
attempts = 1

while compnum != number :
    if number > compnum :
        print("Your guess is too high")
    else : # must be lower than
        print("Your guess is too low")
    number = int(input("Enter number: "))
    attempts += 1

print("Well done, you took", attempts, "attempts")