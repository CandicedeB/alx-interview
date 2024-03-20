#!/usr/bin/python3

"""
    Method that decides number of minimum operations given n characters
"""


def minOperations(n):
    """
        Function that calculates fewest number of operations
        required to give a result exactly n H characters in a file
        args: n: Number of characters displayed
        return:
               number of min operations
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
