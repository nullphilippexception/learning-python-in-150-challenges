number1 = int(input("Enter number: "))
number2 = int(input("Enter another number: "))

# this could already be put into while loop
total = number1 + number2
answer = input("Type \"y\" if you want to input another number: ")

while answer == "y" :
    total += int(input("Enter number: "))
    answer = input("Type \"y\" if you want to input yet another number: ")

print("The total sum of your numbers is", total)