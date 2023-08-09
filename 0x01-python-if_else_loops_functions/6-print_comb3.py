#!/usr/bin/python3
for number in range(10):
    for num in range(number + 1, 10):
        print("{:d}{:d}".format(number, num), end="")
        if number != 8 or num != 9:
            print(", ", end="")
print()
