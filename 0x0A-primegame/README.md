# Prime Number Game

This Python script determines the winner of a prime number game where players take turns selecting prime numbers from a set of consecutive integers.

## Overview

In this game, two players, Maria and Ben, play x rounds. Each round, they choose prime numbers from a set of consecutive integers starting from 1 up to and including n. The player who cannot make a move loses the game. Maria always plays first, and both players play optimally.

## How to Use

1. Clone the repository `git clone https://github.com/ManNjoro/alx-interview.git` or download the script `0-prime_game.py`.
2. Ensure you have Python 3 installed on your system.
3. Run the script with the command `python3 0-prime_game.py`.
4. You can modify the test case in the script to input your own rounds and sets of integers.

## Functionality

The script contains the following functions:

- `generate_primes(n)`: Generates prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.
- `isWinner(x, nums)`: Determines the winner of the prime number game for multiple rounds.

## Usage

```python
from 0-prime_game import isWinner

# Example usage
print(isWinner(5, [2, 5, 1, 4, 3]))  # Output: Ben
