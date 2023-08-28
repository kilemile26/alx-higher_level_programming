#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        result = None  # Handle the case when division by zero occurs
    finally:
        print("Inside result: {}".format(result))  # Print the result in the finally block
        return result  # Return the result
