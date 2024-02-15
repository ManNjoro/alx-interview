#!/usr/bin/python3
"""
This script defines a function to determine the winner of a prime number game.
"""


def generate_primes(n):
    """
    Generate prime numbers up to the given limit
    using the Sieve of Eratosthenes algorithm.

    Args:
    - n (int): The upper limit for generating prime numbers.

    Returns:
    - list: A list containing prime numbers up to the limit n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Determine the winner of the prime number game for multiple rounds.

    Args:
    - x (int): The number of rounds.
    - nums (list): An array of integers representing the values
    of n for each round.

    Returns:
    - str or None: The name of the player who won the most rounds,
    or None if there's a tie.
    """
    primes = generate_primes(max(max(nums), 10))
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
