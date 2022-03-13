import random

def high_low():
    high, low = int(input("Pick high number: ")), int(input("Pick low number: "))
    return random.randint(low, high)


def user_guess():
    return int(input("I am thinking of... which number? "))


def main():
    rightguess = False
    comp_num = high_low()
    while rightguess != True:
        user_num = user_guess()
        if comp_num == user_num:
            print("Correct, you win.")
            rightguess = True
        else:
            if comp_num < user_num:
                print("You were too high, try again")
            else:
                print("You were too low, try again")

main()