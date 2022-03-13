print("""1) Square
2) Triangle""") # ugly solution

choice = int(input("Enter a number: "))

if choice == 1 :
    side = int(input("Length of side: "))
    print("Area", side**2)
elif choice == 2 :
    base = int(input("Base of triangle: "))
    height = int(input("Height of triangle: "))
    print("Area", round(float((1/2)*base*height),2))
else :
    print("Error: invalid input")