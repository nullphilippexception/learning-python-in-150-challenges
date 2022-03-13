answer = "yes"
count = 0

while answer.lower() == "yes" :
    name = input("Input name of party guest: ")
    print(name, "has now been invited")
    count += 1
    answer = input("Do you want to invite somebody else? (yes/no): ")

print(count, "people will be coming to the party")