invited = []

for i in range(0, 3):
    guest = input("Invite a person: ")
    invited.append(guest)

answer = input("Do you want to invite more people? (yes/no) : ")

while answer.lower() == "yes":
    guest = input("Invite a person: ")
    invited.append(guest)
    answer = input("Do you want to invite more people? (yes/no) : ")

print("You invited", invited)
name = input("Please enter one of the names on the list: ")
print("Index:", invited.index(name), ", do you still want that person to come to the party?")
answer = input("yes/no: ")
if answer.lower() == "no":
    invited.remove(name)
    print(invited)