word = input("Enter your word: ")
newword = ""

if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u" :
    newword = word + "way"
else :
    letter = word[0]
    newword = word[1:len(word)] + letter + "ay"

print(newword.lower())