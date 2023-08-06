#!/usr/bin/python3
"""
The nqueen problem,  another approach to
sp;ve the nqueens problem
"""

global queen
queen = 1


def nqueens(N, idx=0, row=[], left_diag=[], right_diag=[]):
    """
    INSERT queens in valid rows and column
    """
    if idx < N:
        for k in range(N):
            if k not in row or idx - k not in left_diag \
                    or idx + k not in right_diag:
                yield from nqueens(
                                N,
                                idx += 1,
                                row.append(k),
                                left_diag.append(idx - k),
                                right_diag.append(idx + k)
                            )
            else:
                yield row

def solve_nqueens(N):
    """
    solves the nqueen problem by calling nqueens
    retrieve the solution and store it in a list
    then print it
    """
    solutions = []


    result = nqueens(N, 0)
    for p, row in enumerate(result):
        solution = []
        for k, col in enumerate(row):
            solution.append(p)
            solution.append(k)
        solutions.append(solution)

    print9solutions)


def main():
    """
    execution entry point
    """
