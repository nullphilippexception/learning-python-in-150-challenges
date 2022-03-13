file = open("Names.txt", "a")
file.write("Chris\n")
file.close()

file = open("Names.txt", "r")
print(file.read())