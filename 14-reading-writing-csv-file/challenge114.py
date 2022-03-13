import csv

start, end = int(input("Enter start year: ")), int(input("Enter end year: "))
file = open("Books.csv", "r")

# note: rather solve this with list(reader), way easier! -> see also challenge116
rowCount = 0
for row in file:
    commaCount = 0
    year = ""
    if rowCount > 0:  # to avoid the row with the titles
        for s in row:
            if s == ",":
                commaCount += 1
            elif commaCount == 2:
                year += s
        year = int(year)
        if start <= year <= end:
            print(row)
    rowCount += 1