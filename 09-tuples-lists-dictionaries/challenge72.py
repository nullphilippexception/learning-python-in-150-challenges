subjects = ["Physics", "Chemistry", "Philosophy", "Physical Education", "Math", "Computer Science"]

print(subjects)
chosen = input("Which subject do you not like? ")
subjects.remove(chosen) # error prone
print(subjects)