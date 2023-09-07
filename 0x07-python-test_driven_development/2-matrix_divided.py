#!/usr/bin/python3
def matrix_divided(matrix, div):
    # Check if matrix is list of lists containing ints & floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row has same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number & not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform division & round to 2 decimal places
    result = [[round(num / div, 2) for num in row] for row in matrix]
    
    return result
