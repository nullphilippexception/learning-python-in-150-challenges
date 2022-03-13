file = open("Names.txt", "r")
print(file.read())
selectedName = input("Enter name you don't want to save to new file: ")

file = open("Names.txt", "r")
eligibleNames = []
currentName = ""
for s in file.read():
    if s != "\n":
        currentName += s
    else:
        if len(currentName) > 0 and currentName.lower() != selectedName.lower():  # it is not the name not to be transferred
            eligibleNames.append(currentName)
            currentName = ""  # reset current name
        elif len(currentName) > 0 and currentName.lower() == selectedName.lower():  # it is the name not to be transferred
            currentName = ""  # reset current name

file2 = open("Names2.txt", "w")
if len(eligibleNames) > 0:
    file2.write(eligibleNames[0] + "\n")
    eligibleNames.remove(eligibleNames[0])
    file2.close()

file2 = open("Names2.txt", "a")
for name in eligibleNames:
    file2.write(name + "\n")
file2.close()

