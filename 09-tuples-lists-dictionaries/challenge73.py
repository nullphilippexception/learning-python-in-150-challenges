foods = {}

for i in range(1, 5): # food indices supposed to start with 1
    enteredFood = input("Please enter your food no. " + str(i) + " : ")
    foods[i] = enteredFood

print(foods)
removeFruit = int(input("Which fruit do you want to remove? (enter number) "))
del foods[removeFruit]

print(sorted(foods.values()))