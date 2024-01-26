#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of '#' characters.

    :param size: The size (side length) of the square.
    :raises TypeError: If size is not an integer or is a float.
    :raises ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print("#" * size)
        if i < size - 1:
            print()
