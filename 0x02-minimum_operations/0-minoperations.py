#!/usr/bin/python3
"""
This module contains a function that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
the file is a text file containing only the character H.
the text editor can execute only two operations in the file:
    Copy all the characters.
    Paste all the characters.
"""
from math import sqrt


def minOperations(n):
    """
    Returns the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    result = 0
    if n <= 1:
        return 0
    if n == 2:
        return 2
    while n % 2 == 0:
        result += 2
        n = n / 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            result += i
            n = n / i
    if n > 2:
        result += n
    return int(result)
