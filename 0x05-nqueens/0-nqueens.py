#!/usr/bin/python3
"""
Solve the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Validate a queen in the same column
    """
    for i in range(row):
        if board[i] == col:
            return False

    """
    Validate a queen in the same diagonal
    """
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_nqueens(n, board, row):
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)


if __name__ == "__main__":
    """
    Validate the number of arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """
    Validate value of N from cli
    """
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """
    Validate value of N
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(n, board, 0)
