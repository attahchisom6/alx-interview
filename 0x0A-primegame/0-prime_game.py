#!/usr/bin/python3
"""
A prime game
"""


def isWinner(x, nums):
    """
    A game where Maria and Ben start oy pick a prime number and then removing
    mutiples of the prime number
    the first to have no more prime number to choose looses out
    @params:
        @x: Number of rounds played by both friends
        @nums: a list of n, for each round
    """
    def is_prime(num):
        """
        checks  if num is a prime
        """
        if num <= 1:
            return False

        for k in range(2, int(n ** 0.5) + 1):
            if num % k == 0:
                return False
        return True

    winner_list = [None] * x

    if nums is None or nums == []:
        return None
    if x is None or x == 0:
        return None

    for k in range(x):
        n = nums[k]

        prime_list = [p for p in range(2, n + 1) if is_prime(p)]

        if len(prime_list) % 2 != 0:
            winner_list[k] = "Maria"
        else:
            winner_list[k] = "Ben"

    Maria_wins = winner_list.count('Maria')
    Ben_wins = winner_list.count('Ben')

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
