people = int(input("How many people do you want to invite: "))

if people < 10 :
    for i in range(0, people) :
        name = input("Enter guest's name: ")
        print(name,"has been invited")
else :
    print("Too many people")