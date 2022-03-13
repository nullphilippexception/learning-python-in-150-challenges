import random


def addition():
    num1, num2 = random.randint(5, 25), random.randint(5, 25)
    correct = num1 + num2
    answer = int(input("What is " + str(num1) + " + " + str(num2) + " ? "))
    result = (answer, correct)
    return result


def subtraction():
    num1, num2 = random.randint(25, 50), random.randint(1, 50)
    correct = num1 - num2
    answer = int(input("What is " + str(num1) + " - " + str(num2) + " ? "))
    result = (answer, correct)
    return result


def result_check(user_result, true_result):
    if user_result == true_result:
        print("Correct")
    else:
        print("Incorrect, the answer is", true_result)


def main():
    print("1) Addition")
    print("2) Subtraction")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        user_result, true_result = addition()
        result_check(user_result, true_result)
    elif choice == "2":
        user_result, true_result = subtraction()
        result_check(user_result, true_result)
    else:
        print("This is not a valid choice")


main()
