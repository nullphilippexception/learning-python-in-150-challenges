import random

numbers = []

for i in range(0, 3):
    numbers.append(random.randint(100, 999))

# task is to use this functionality, therefore don't include it in previous loop
for nr in numbers:
    print(nr)

userNumber = int(input("Enter a number: "))

if userNumber in numbers:
    print("Index is", numbers.index(userNumber))
else:
    print("That is not in the list")