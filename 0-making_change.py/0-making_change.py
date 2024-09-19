#!/usr/bin/python3
"""
Making change module"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.

    Arguments:
    coins -- list of integers with the values of the coins
    total -- the total amount of money

    Return:
    The fewest number of coins needed to meet the total amount
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return (0)
    
    # sort the coins in a descending order
    coins.sort(reverse=True)
    #initialize the number of coins variable
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return (-1)
    return (num_coins)
