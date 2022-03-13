def num_getter():
    num = int(input("Enter a number: "))
    return num


def num_counter(num):
    for i in range(1, num + 1):
        print(i)


def main():
    num = num_getter()
    num_counter(num)


main()
