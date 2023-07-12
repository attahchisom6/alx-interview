#!/usr/bin/python3
"""
minimum operation to reach a given number of character
"""



def minOperations(n):
    """
    method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor < n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
