from array import *
import random

randarr = array('i', [])
for i in range(0, 5):
    randarr.append(random.randint(0, 50))

userarr = array('i', [])
for i in range(0, 3):
    userarr.append(int(input("Enter number: ")))

randarr.extend(userarr)
randarr = sorted(randarr)

for nr in randarr:
    print(nr)