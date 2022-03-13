from array import *
import random

arr = array('i', [])

for i in range(0, 5):
    arr.append(random.randint(0, 100))

for nr in arr:
    print(nr)