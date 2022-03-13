import csv

# function to store an additional name to csv
def store_name():
    file = open("Salaries.csv", "a")
    name, salary = input("Enter name: "), input("Enter salary: ")
    file.write(name + "," + salary + "\n")
    file.close()

# function to display all names in the csv
def displays_name():
    file = open("Salaries.csv", "r")
    reader = csv.reader(file)
    lst = list(reader)
    for row in lst:
        print(row)
    file.close()

# main program loop
def main():
    cont = True
    try:
        file = open("Salaries.csv", "x")
        file.write("Name,Salaries\n")
        file.close()
    except FileExistsError:
        print()  # no need to print anything, everything is fine because file exists

    while cont != False:
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit program")
        choice = input("Enter the number of your selection: ")

        if choice == "1":
            store_name()
        elif choice == "2":
            displays_name()
        elif choice == "3":
            cont = False
        else:
            print("Not a valid choice")

main()