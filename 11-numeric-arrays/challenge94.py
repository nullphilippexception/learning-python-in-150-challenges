from array import *

arr = array('i', [])

for i in range(0, 5):
    arr.append(int(input("Please enter number: ")))

pos = -1

while pos == -1:
    sel = int(input("Select number from array: "))
    if arr.count(sel) > 0:
        pos = arr.index(sel)
    else:
        print("Not a valid item, try again")

print("Your item has index:", str(pos))