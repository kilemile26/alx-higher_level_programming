#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

def main():
    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    main()
