#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Parameters:
    x (int): The number of rounds.
    nums: A list of integers representing the upper limit of numbers
    for each round.

    Returns:
    str: The name of the winner ("Ben" or "Maria") or None if there is a tie.

    The game is played as follows:
    - For each round, a number n is taken from the list nums.
    - If n is 1, Ben wins the round.
    - For numbers greater than 1, a list of prime numbers up to n is generated.
    - If the count of prime numbers is even, Ben wins the round.
    - If the count of prime numbers is odd, Maria wins the round.
    - The player with the most wins is declared the overall winner.
    """
    if x is None or nums is None or len(nums) != x:
        return None
    ben = 0
    maria = 0
    for n in nums:
        if n == 1:
            ben += 1
            continue
        prime = [True for i in range(n + 1)]
        prime[0] = False
        prime[1] = False

        for i in range(2, n + 1):
            if prime[i]:
                for y in range(i * i, n + 1, i):
                    prime[y] = False
        primes = [i for i in range(0, n + 1) if prime[i]]

        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
