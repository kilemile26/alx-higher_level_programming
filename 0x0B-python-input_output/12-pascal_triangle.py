#!/usr/bin/python3
"""
module that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Each row starts with 1

        for j in range(1, i):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)

        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)

    return triangle


# Example usage:
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
