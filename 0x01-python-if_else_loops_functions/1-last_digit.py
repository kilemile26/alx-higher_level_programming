#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number*-1) % 10*-1
output = "Last digit of {} is {} and is".format(number, last)
if last > 5:
    print(output + " greater than 5")
elif last == 0:
    print(output + " 0")
else:
    print(output + " less than 6 and not 0")
