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
    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
        operations += 1
        current += clipboard

    if current == n:
        return operations
    else:
        return 0
