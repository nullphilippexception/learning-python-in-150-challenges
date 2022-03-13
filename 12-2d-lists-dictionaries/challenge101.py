dict_2d = {"John": {"N" : 3056, "S" : 8463, "E" : 8441, "W" : 2694}, "Tom": {"N" : 4832, "S" : 6786, "E" : 4737, "W" : 3612},
           "Anne": {"N" : 5239, "S" : 4802, "E" : 5820, "W" : 1859}, "Fiona": {"N" : 3904, "S" : 3645, "E": 8821, "W" : 2451}}

print(dict_2d)

selName, selReg = input("Select a name: "), input("Select a region: ")
print(dict_2d[selName][selReg])
newVal = int(input("Enter new value for this field: "))

dict_2d[selName][selReg] = newVal
print(dict_2d[selName])