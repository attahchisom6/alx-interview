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

        for k in range(2, n + 1):
            if num % k == 0:
                return False
        return True

    winner_list = [None] * (len(nums) + 1)

    if nums is None or nums == []:
        return None
    if x is None or x == 0:
        return None

    for n in range(x):
        if winner_list[n] is not None:
            continue

        if is_prime(n):
            winner_list[n] = "Maria"
        else:
            winner_list[n] = "Ben"

    Maria_wins = winner_list.count('Maria')
    Ben_wins = winner_list.count('Ben')

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None
