# unclear where postal codes contain letters -> maybe US? but would be redundant with unique numbers?

postal = input("Please input postal code with first two chars being letters not numbers: ")

for i in range(0, len(postal)):
    if i <= 1:
        print(end=postal[i].upper())
    else:
        print(end=postal[i])