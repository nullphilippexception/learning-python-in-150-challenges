countries = ("Germany", "Austria", "Belgium", "Switzerland", "Canada")

print(countries)
chosen = input("Select one country: ")
print(countries.index(chosen.title()))

nr = int(input("Now enter a number (0 to 4): "))
print(countries[nr])