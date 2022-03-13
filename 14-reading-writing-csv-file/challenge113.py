import csv

rec = int(input("How many records do you want to add? "))

for i in range(0, rec):
    newBook = input("Enter new title: ") + "," + input("Enter new author: ") + "," + input("Enter new year: ")
    file = open("Books.csv", "a")
    file.write(newBook)
    file.close()

author = input("Choose an author whose books you want to display: ")

file = open("Books.csv", "r")
printCount = 0
for row in file:
    if author.lower() in row.lower():
        print(row)
        printCount += 1

if printCount == 0:
    print("No books by this author available")