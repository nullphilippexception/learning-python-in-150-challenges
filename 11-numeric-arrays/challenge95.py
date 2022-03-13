from array import *

arr = array('d', [10.29, 25.31, 30.45, 49.66, 75.89])

nr = int(input("Enter whole number between 2 and 5: "))

while nr < 2 or nr > 5:
    nr = int(input("Number not valid, enter whole number between 2 and 5"))

for i in range(0, 5):
    print(round(arr[i]/nr, 2))