from array import *

arr = array('i', [])

for i in range(0, 5):
    arr.append(int(input("Enter number: ")))

arr = sorted(arr)
print(arr)
rem = int(input("Select one number to be removed: "))

arr.remove(rem)
newarr = array('i', [rem])

print("Old array", arr)
print("New array", newarr)