#!/usr/bin/python3
for char_code in range(122, 96, -1):
    print("{}".format(chr(char_code).swapcase()), end="")
