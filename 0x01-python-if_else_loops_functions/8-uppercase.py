#!/usr/bin/python3
def uppercase(str):
    if ord(str) in range(97, 123):
        print ("{}".format(chr(ord(str) - 32)))
    else:
        print("{}".format(str))
