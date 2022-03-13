print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = input("Make a selection 1, 2 or 3: ")

if selection != "1" and selection != "2" and selection != "3":
    print("Invalid input")
elif selection == "1":
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()
elif selection == "2":
    file = open("Subject.txt", "r")
    print(file.read())
elif selection == "3":  # has to be the case
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "a")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())