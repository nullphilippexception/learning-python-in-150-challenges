programmes = ["NFL", "Bundesliga", "South Park", "Rick & Morty"]
print(programmes)

newShow = input("Enter a new show: ")
pos = int(input("Enter position for new show: "))
programmes.insert(pos, newShow)

print(programmes)