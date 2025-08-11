#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
# This code squares each element in a matrix using nested map functions.
# The outer map applies to each row, and the inner map applies to each element in the row.
