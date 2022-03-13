def showList(lst):
    for name in lst:
        print(name)


def addName(lst):
    lst.append(input("Please enter new name: "))
    return lst


def changeName(lst):
    change_index, new_value = int(input("Please enter index of name to be changed: ")), input("Please enter the changed name: ")
    lst[change_index] = new_value
    return lst


def deleteName(lst):
    delete_element = input("Enter name to be deleted: ")
    lst.remove(delete_element)
    return lst


def main():
    end = False
    lst = []
    while end != True:
        choice = input("Pick an option: 1) Display list, 2) Add name, 3) Change name, 4) Delete name, 5) End program: ")
        if choice == "1":
            showList(lst)
        elif choice == "2":
            lst = addName(lst)
        elif choice == "3":
            lst = changeName(lst)
        elif choice == "4":
            lst = deleteName(lst)
        elif choice == "5":
            end = True
        else:
            print("This is not a valid choice")

main()
