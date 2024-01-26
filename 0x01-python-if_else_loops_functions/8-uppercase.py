#!/usr/bin/python3
def uppercase(str):
    n = ""
    for c in str:
        if ord(c) in range(97, 123):
            n += chr(ord(c) - 32)
        else:
            n += c
    print("{}".format(n))
