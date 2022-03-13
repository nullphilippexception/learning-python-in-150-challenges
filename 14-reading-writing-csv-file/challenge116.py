import csv

# read from old csv
file = open("Books.csv", "r")
reader = csv.reader(file)
rows = list(reader)
file.close()

# print old csv
for row in rows:
    print(row)

# get things that are to be changed
deleteRow, changeRow = int(input("Select a row you want to delete (count starts at 1): ")), int(input("Select a row you want to change (count starts at 1): "))

# change row
rows[changeRow][0] = input("New title for selected row: ")
rows[changeRow][1] = input("New author for selected row: ")
rows[changeRow][2] = input("New year for selected row: ")

# recreate the file including the edits (simply don't insert row to be deleted)
file = open("Books.csv", "w")
rowCount = 0
for row in rows:
    if rowCount != deleteRow:
        file.write(row[0] + "," + row[1] + "," + row[2] + "\n")
    rowCount += 1
