#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    """
    triangle = []

    if n > 0:
        for i in range(n):
            row = []
            coefficient = 1

            for j in range(i + 1):
                row.append(coefficient)
                coefficient = coefficient * (i - j) // (j + 1)

            triangle.append(row)

    return triangle
