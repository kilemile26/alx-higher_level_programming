#!/usr/bin/python3
def fizzbuzz():
    result = ""
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result += "FizzBuzz "
        elif number % 5 == 0:
            result += "Buzz "
        elif number % 3 == 0:
            result += "Fizz "
        else:
            result += str(number) + " "

    return result.strip()

# Now you can call the fizzbuzz() function without immediate printing
output = fizzbuzz()
#print(output)
