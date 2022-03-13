from array import *

arr = array('i', [1,2,1,2,3])
print(arr)

nr = int(input("Enter one of the numbers from the array: "))
print("This number appears", str(arr.count(nr)), "time(s)")

