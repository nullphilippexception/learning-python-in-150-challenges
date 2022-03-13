sentence = "This is the sentence you will see, it's length is 52"
start = int(input("Enter start point: "))
end = int(input("Enter end point: "))

print(sentence[start+1:end])  # exercise not clear whether to include/exclude start & end: here exclusive solution
