#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    def rotate_2d_matrix(matrix):

    Rotate a 2D matrix 90 degrees clockwise in place.

    This function takes a square matrix and rotates it 90 degrees clockwise.
    The rotation is done in place.

    Parameters:
    matrix (List[List[int]]): A 2D list representing the square matrix.
    """
    n = len(matrix)
    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] =\
                matrix[i][n - 1 - j], matrix[i][j]
