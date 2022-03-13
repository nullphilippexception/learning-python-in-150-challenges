dict = {}

for i in range(0, 4):
    name, age, shoesize = input("Enter a name: "), int(input("Enter an age: ")), int(input("Enter a shoe size: "))
    dict[name] = {"Age" : age, "Shoe size" : shoesize}

selName = input("Enter a name from the list: ")
print(dict[selName])
print(dict)