#!/usr/bin/python3
"""
minimum operation to reach a given number of character
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    operations = 0
    factor = 2

    if n <= 1:
        return operations
    while factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print(
            "min Number of operations to reach {} char: {}"
            .format(n, minOperations(n)))

    n = 12
    print(
            "min Number of operations to reach {} char: {}"
            .format(n, minOperations(n)))

    n = 13
    print(
            "min Number of operations to reach {} char: {}"
            .format(n, minOperations(n)))
