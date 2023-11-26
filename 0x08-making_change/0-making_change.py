#!/usr/bin/python3
"""
Module determines fewest coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for val in range(coin, total + 1):
            min_coins[val] = min(min_coins[val], min_coins[val - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
