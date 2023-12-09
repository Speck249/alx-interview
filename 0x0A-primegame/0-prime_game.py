#!/usr/bin/python3
"""
Determine winner of
Prime Game.
"""


def isWinner(x, nums):
    """
    Method determines the winner
    of a Prime Game.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        """
        Build a list of Prime numbers
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        primes = get_primes_up_to_n(n)
        maria_turn = True

        while primes:
            if maria_turn:
                selected = min(primes)
            else:
                selected = max(primes)

            primes = [num for num in primes if num % selected != 0]
            maria_turn = not maria_turn

        return 'Maria' if not maria_turn else 'Ben'
    """
    Play each round and count wins.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    """
    Determine the winner of the game.
    """
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
