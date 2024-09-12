#!/usr/bin/python3
"""
Module for rotating a 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise.

    Args:
        matrix: A list of integers.
    Returns:
        None.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
