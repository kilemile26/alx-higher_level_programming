#!/usr/bin/python3
"""
Lazy matrix multiplication module using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the result.
    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: The product of the two matrices.

    Raises:
        ValueError: If matrices can't be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_a must be a list of lists or m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) \
            or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise ValueError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    result = np.dot(matrix_a, matrix_b)

    return result.tolist()
