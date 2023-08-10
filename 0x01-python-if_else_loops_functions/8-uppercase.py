#!/usr/bin/python3
def uppercase(str):
    if ord(str) in range(97, 123):
        print (ord(str) - 35)
    else:
        print(ord(str))
