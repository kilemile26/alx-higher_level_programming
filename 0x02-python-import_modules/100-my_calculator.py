#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div 
    import sys


    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if  sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


    print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
