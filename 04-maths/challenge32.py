import math

radius = int(input("Enter radius: "))
depth = int(input("Enter depth: "))

volume = round(math.pi*(radius**2)*depth,3)
print("Volume:",volume)