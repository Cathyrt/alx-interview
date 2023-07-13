#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n 'H' characters in the file.

    Args:
        n: An integer representing the desired number of 'H' characters.

    Returns:
        The fewest number of operations required,
        or 0.
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
