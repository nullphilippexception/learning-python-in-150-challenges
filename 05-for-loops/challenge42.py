total = 0

for i in range(0, 5) :
    currentNumber = int(input("Enter number: "))
    choice = input("Want to include that number? (yes/no): ")
    if choice.lower() == "yes" :
        total += currentNumber

print("Total is:", total)