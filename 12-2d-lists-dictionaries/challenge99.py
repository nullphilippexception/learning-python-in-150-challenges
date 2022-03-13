list_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list_2d)

selRow = int(input("Select row to be displayed: "))
print(list_2d[selRow])

selCol = int(input("Select a column for this row: "))
print(list_2d[selRow][selCol])
answer = input("Do you want to change this value? (yes/no) : ")
if answer.lower() == "yes":
    newVal = int(input("Enter new value: "))
    list_2d[selRow][selCol] = newVal

print(list_2d[selRow])
