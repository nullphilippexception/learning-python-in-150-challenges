firstname = input("Enter firstname: ")

if len(firstname) < 5 :
    surname = input("Enter surname: ")
    wholename = firstname + surname
    print(wholename.upper())
else :
    print(firstname.lower())