#!/usr/bin/python3#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    arg_tot = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            arg_tot += int(arg)
    print(arg_tot)
