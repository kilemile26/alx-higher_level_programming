#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
output = "Last digit of {} is {} and is".format(number, last)

if last > 5:
    outtput += " greater than 5"
elif last == 0:
    output += " 0"
else:
    output += " less than 6 and not 0"
