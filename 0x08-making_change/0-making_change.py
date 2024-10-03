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

    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for i in range(1, total + 1):

        for j in range(0, len(coins)):

            if coins[j] <= i:

                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    return -1 if dp[total] > total else dp[total]
