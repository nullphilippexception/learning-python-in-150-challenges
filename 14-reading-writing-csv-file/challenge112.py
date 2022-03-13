import csv

newBook = input("Enter new title: ") + "," + input("Enter new author: ") + "," + input("Enter new year: ")

file = open("Books.csv", "a")
file.write(newBook)
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)