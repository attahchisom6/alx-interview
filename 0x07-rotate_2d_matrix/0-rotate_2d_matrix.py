#!/usr/bin/python3
"""
A program to rotate a matrix 90 degree clockwisely, we achieve this by
1. interate through the row and column of the matrix, then set the element at
row p and column k to be at row k and
columb p, the element at row k and column p to be at row p and column k
thus effectively reflecting the element at each side of the diagonal

2. we iterate through each row in the natrix and reverse it
"""


def rotate_2d_matrix(matrix):
    """
    rotate a matrix 90 clockwisely
    """
    lenn = len(matrix)
    for p in range(lenn):
        for k in range(p):
            temp = matrix[p][k]
            matrix[p][k] = matrix[k][p]
            matrix[k][p] = temp

    for row in matrix:
        row.reverse()

    return matrix
