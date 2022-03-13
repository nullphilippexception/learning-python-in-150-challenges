name = input("Enter name: ")
number = int(input("Enter number: "))
output = ""

if number < 10 :
    output = name
else :
    output = "Too high"
    number = 3

for i in range(0, number) :
    print(output)