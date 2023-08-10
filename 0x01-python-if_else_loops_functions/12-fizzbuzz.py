#!/usr/bin/python3
def fizzbuzz():
    for number in range (101):
        if number % 3:
            print("Fizz")
        elif number % 5:
            print ("Buzz")
        elif number % 3 and number % 5:
            print("FizzBuzz")
        else:
            print(number)
