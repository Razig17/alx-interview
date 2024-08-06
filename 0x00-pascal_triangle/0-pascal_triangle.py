#!/usr/bin/python3

"""
This module contains a function to generate Pascal's triangle.

Pascal's triangle is a triangular array of binomial coefficients.
Each number in the triangle is the sum of
the two numbers directly above it.

This module provides the following function:
- pascal_triangle(n): Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Examples:
        >>> pascal_triangle(0)
        []
        >>> pascal_triangle(1)
        [[1]]
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            if j == i or j == 0:
                row.append(1)
            else:
                row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
        pascal.append(row)
    return pascal
