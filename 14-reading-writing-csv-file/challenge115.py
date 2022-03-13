import csv

file = open("Books.csv", "r")
count = 0
for row in file:
    if count == 0:
        print(row)
    else:
        print(str(count), row)
    count += 1