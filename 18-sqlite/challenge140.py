import sqlite3
# connect to db
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

# function that displays the menu to the user and returns their choice
def displayMenu():
    print("Main menu")
    print("1) View phone book")
    print("2) Add to phone book")
    print("3) Search for surname")
    print("4) Delete person from phonebook")
    print("5) Quit")
    return input("Enter your selection: ")

# function that displays the phonebook
def displayPhonebook():
    cursor.execute("SELECT * FROM Names")
    for person in cursor.fetchall():
        print(person)

# function that lets user add person to database
def addPerson():
    id, firstname, surname, number = input("Id: "), input("First name: "), input("Surname: "), input("Phone number: ")
    cursor.execute("""INSERT INTO Names (id,first_name,surname,phone_number) VALUES
                    (?,?,?,?)""", (id, firstname, surname, number))
    db.commit()

# function that lets user search for a person in the database
def searchPerson():
    search_surname = input("Please enter surname you want to search for: ")
    cursor.execute("SELECT * FROM Names WHERE surname=?", [search_surname])
    for person in cursor.fetchall():
        print(person)

# function that lets user delete a person from the database
def deletePerson():
    delete_id = int(input("Enter id of person you want to delete: "))
    cursor.execute("DELETE FROM Names WHERE id=?", [delete_id])
    db.commit()

# main loop of the program
def main():
    endProgram = False
    while endProgram == False:
        choice = displayMenu()
        if choice == "1":
            displayPhonebook()
        elif choice == "2":
            addPerson()
        elif choice == "3":
            searchPerson()
        elif choice == "4":
            deletePerson()
        elif choice == "5":
            endProgram = True
        else:
            print("Invalid selection, try again")

# execute
main()
