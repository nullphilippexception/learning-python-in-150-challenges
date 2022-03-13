again = True

while again :
    number = int(input("Enter number between 10 and 20 (inclusive): "))
    if number < 10 :
        print("Too low")
    elif number > 20 :
        print("Too high")
    else :
        again = False
        print("Thank you")