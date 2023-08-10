#!/usr/bin/python3
def fizzbuzz():
    result = ""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result += "FizzBuzz "
#            #print("FizzBuzz ", end="")
        elif number % 5 == 0:
            result += "Buzz "
#            #print("Buzz ", end="")
        elif number % 3 == 0:
            result += "Fizz "
#            #print("Fizz ", end="")
        else:
            result += str(number) + " "
#            #print(number, "", end="")
    return result.strip()
fizzbuzz()
