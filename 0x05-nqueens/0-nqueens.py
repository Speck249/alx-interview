#!/usr/bin/python3
"""
Solution for N queens problem
"""
import sys


def find_chessboard_solution(rows, col):
    """
    Solve N x N chessboard
    """
    solution = [[]]
    for chess_piece in range(rows):
        solution = position_chess_piece(chess_piece, col, solution)
    return solution


def position_chess_piece(chess_piece, col, initial_output):
    """
    Place chess piece at a certain position
    """
    safe_positions = []
    for arrangement in initial_output:
        for i in range(col):
            if is_safe(chess_piece, i, arrangement):
                safe_positions.append(arrangement + [i])
    return safe_positions


def is_safe(chess_piece, i, arrangement):
    """
    Validate safe move
    """
    return not any(abs(arrangement[column] - i)
                   == chess_piece - column or i
                   == arrangement[column]
                   for column in range(chess_piece))


def initialize_chess_game():
    """
    Initialize chess game
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n_rows = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n_rows < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n_rows


def main():
    """
    Main entry point of program
    """
    rows_count = initialize_chess_game()
    solutions = find_chessboard_solution(rows_count, rows_count)
    output = []
    for arrangement in solutions:
        output.append([[chess_piece, i] for chess_piece, i in
                       enumerate(arrangement)])
    return output


if __name__ == '__main__':
    result = main()
    for clean in result:
        print(clean)
