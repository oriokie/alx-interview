#!/usr/bin/python3
"""
0-prime_game.py: Solution for the Prime Game problem.

This module contains the implementation of the isWinner function,
which determines the winner of multiple rounds of the Prime Game.
"""


def generate_primes(max_n):
    """
    Generate a list of prime numbers up to max_n using the
    Sieve of Eratosthenes.

    Args:
    max_n (int): The upper limit for generating prime numbers.

    Returns:
    list: A boolean list where index i is True if i is prime, False otherwise.
    """
    sieve = [True] * (max_n + 1)  # Initialize all numbers as prime
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:  # i is prime
            # Mark all multiples of i as not prime
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return sieve  # sieve[i] is True if i is prime, False otherwise


def winner_for_n(n, primes):
    """
    Determine the winner for a single game with n integers.

    Args:
    n (int): The upper limit of integers for this game.
    primes (list): A pre-computed list of prime numbers.

    Returns:
    str: "Maria" if she wins, "Ben" if he wins.
    """
    prime_count = sum(primes[:n + 1])
    return "Maria" if prime_count % 2 == 1 else "Ben"


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the Prime Game.

    Args:
    x (int): The number of rounds.
    nums (list): A list of n values for each round.

    Returns:
    str or None: Name of the player with the most wins, or None if it's a tie.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = generate_primes(max_n)

    maria_wins = ben_wins = 0
    for n in nums[:x]:  # Ensure we only play 'x' rounds
        winner = winner_for_n(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
