#!/usr/bin/python3#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    total = sum(int(arg) for arg in sys.arg[1:])
    print("{}".format(total))
