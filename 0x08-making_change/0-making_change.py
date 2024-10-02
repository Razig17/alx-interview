#!/usr/bin/python3
"""This module contain makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.


    Parameters:
    coins A list of integers representing the values of the coins.
    total (int): The total amount to be met using the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
    If the total is 0 or less, returns 0.
    If the total cannot be met by any combination of the coins, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    print(coins)
    if total < coins[0]:
        return -1

    count = 0
    for coin in coins:
        count += total // coin
        total = total % coin
        if total == 0:
            return count

    return -1
