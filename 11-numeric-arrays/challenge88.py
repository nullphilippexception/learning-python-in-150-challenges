from array import *

arr = array('i', [])

for i in range(0, 5):
    nr = int(input("Enter number: "))
    arr.append(nr)

arr = sorted(arr)
arr.reverse()
print(arr)