from array import *

arr = array('i', [])

while len(arr) < 5:
    nr = int(input("Please enter a number between 10 and 20: "))
    if 10 <= nr <= 20:
        arr.append(nr)
    else:
        print("Outside the range")

print("Thank you")
for nr in arr:
    print(nr)