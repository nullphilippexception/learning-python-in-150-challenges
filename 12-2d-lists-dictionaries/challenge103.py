dict = {}

for i in range(0, 4):
    name, age, shoesize = input("Enter a name: "), int(input("Enter an age: ")), int(input("Enter a shoe size: "))
    dict[name] = {"Age" : age, "Shoe size" : shoesize}

for name in dict:
    print(name, dict[name]["Age"])