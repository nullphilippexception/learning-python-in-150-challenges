bottles = 10

while bottles > 0 :
    print("There are", bottles, "green bootles hanging on the wall,", bottles, "green bottles hanging on the wall and if 1 green bottle should accidentally fall")
    answer = int(input("how many green bottles will be hanging on the wall? "))
    while answer != bottles - 1 :
        answer = int(input("No, try again: "))
    print("There will be", answer, "green bottles hanging on the wall")
    bottles -= 1

print("There are no more green bottles hanging on the wall")