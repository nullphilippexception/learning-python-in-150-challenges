nums = []

for i in range(0, 3):
    nr = int(input("Enter a number: "))
    nums.append(nr)
    print(nums)

answer = input("Still want to save last number? (yes/no): ")
if answer.lower() == "no":
    nums.pop()

print(nums)