#!/usr/bin/python3
def uppercase(str):
    if str and ord(str) in range(97, 123):
        print ("{}".format(chr(ord(str) - 32)))
    else:
        print("{}".format(str))
