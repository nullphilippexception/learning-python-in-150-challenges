invited = []

for i in range(0, 3):
    guest = input("Invite a person: ")
    invited.append(guest)

answer = input("Do you want to invite more people? (yes/no) : ")

while answer.lower() == "yes":
    guest = input("Invite a person: ")
    invited.append(guest)
    answer = input("Do you want to invite more people? (yes/no) : ")

print("You invited", len(invited))