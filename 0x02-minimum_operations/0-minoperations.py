#!/usr/bin/python3
"""
Module calculates fewest number
of operations needed to result
in exactly n H characters in a file.
"""


def minOperations(n):
    """
    Method Returns an integer
    If n is impossible to achieve, returns 0
    """
    if n < 2:
        return 0

    operations = 0
    current = 2

    while current <= n:
        if n % current == 0:
            operations += current
            n = n // current
            current -= 1
        current += 1

    return operations
