#!/usr/bin/python3
def uppercase(str):
    n = ""
    for c in str:
        if str and ord(str) in range(97, 123):
            n += chr(ord(s) - 32)
        else:
            n += c
    print(n)
