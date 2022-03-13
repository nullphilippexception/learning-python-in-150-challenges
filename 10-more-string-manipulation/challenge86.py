password1 = input("Enter a new password: ")
password2 = input("Enter it again: ")

if password1 != password2 and password1.lower() != password2.lower():  # second part will always be true if first part true except edge case checked in else
    print("Incorrect")
else:
    if password1 != password2 and password1.lower() == password2.lower():
        print("They must be the same case")
    else:
        print("Thank you")

