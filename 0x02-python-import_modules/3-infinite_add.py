#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_tot = 0
    for arg in sys.argv[1:]:
        arg_tot += int(arg)
    print(arg_tot)
