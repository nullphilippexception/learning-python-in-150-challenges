direction = input("Enter direction: ")

if direction.lower() == "up" :
    topnr = int(input("Enter top number: "))
    for i in range(1, topnr + 1) :
        print(i)
elif direction.lower() == "down" :
    downnr = int(input("Enter a number below 20: "))
    for i in range(20, downnr - 1, -1) :
        print(i)
else :
    print("I don't understand")