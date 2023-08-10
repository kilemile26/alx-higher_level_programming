#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result += "FizzBuzz "
        elif number % 5 == 0:
            result += "Buzz "
        elif number % 3 == 0:
            result += "Fizz "
        else:
            print(number, "", end="")


fizzbuzz()
