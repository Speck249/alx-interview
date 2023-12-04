#!/usr/bin/python3
"""
Determine the winner of
the Prime Game.
"""


def isWinner(x, nums):
    """
    Function check if number is prime.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_next_prime(n):
        n += 1
        while not is_prime(n):
            n += 1
        return n

    def determine_round_winner(n):
        prime = 2  # Start with the first prime number
        while prime <= n:
            n -= n // prime
            prime = get_next_prime(prime)
        return "Maria" if n % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = determine_round_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
