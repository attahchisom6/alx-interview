#!/usr/bin/python3
"""
generating a pascal triangle
"""


def pascal_triangle(numRows):
    """
    this function will create list of list that will represent a pascal
    triangle
    """
    if numRows <= 0:
        return []

    triangle = []
    for p in range(numRows):
        row = []
        for k in range(p + 1):
            if k == 0 or k == p:
                row.append(1)
            else:
                row.append(triangle[p - 1][k - 1] + triangle[p - 1][k])
        triangle.append(row)
    return triangle
