name = input("Please enter your name: ")
vowelCount = 0

for s in name:
    if s.lower() == "a" or s.lower() == "e" or s.lower() == "i" or s.lower() == "o" or s.lower() == "u":
        vowelCount = vowelCount + 1

print("Amount of vowels in your name:", vowelCount)