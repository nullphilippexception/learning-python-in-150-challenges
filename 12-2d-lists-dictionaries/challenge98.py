list_2d = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list_2d)

selRow = int(input("Select row to be displayed: "))

print(list_2d[selRow])
newVal = int(input("Enter value to be added: "))
list_2d[selRow].append(newVal)

print(list_2d)
