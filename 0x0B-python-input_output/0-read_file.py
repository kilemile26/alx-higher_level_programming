#!/usr/bin/python3
"""module for reading file and printing to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
