#!/usr/python3
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
    for value in range(coin, total + 1):
      min_coins[value] = min(min_coins[value], min_coins[value - coin] + 1)
  
  return min_coins[total] if min_coins[total] != float('inf') else -1
