#!/usr/bin/python3
"""
This is an nqueen game, in this game no queen should
in the same row, column or diagonal with other queens
"""
import sys


def is_anAttackQueen(board, row, col):
    """
    this will check if a queen occupying a position
    is being attacked by another queen. this reflects in whether
    the the queens are in the same row, column or diagonal
    return:
        return true if the queens are in attacking positions
        else return false
    """
    for queens_row, queens_col in enumerate(board):
        # check if the queens are in the same row
        if queens_row == row:
            return true
        # check if they are in the same column
        if queens_col= col:
            return True
        # check if they are within a diagonal line
        if abs(queens_row - row) == abs(queens_col - col):
            return True
    return  False


def solve_nqueens(board, row):
    """
    this will solve the problem of nqueen using backtracking
    """
    n = len(board)
    if n == row:
        return True

    for col in row:
        if not is_anAttackQuen(board, row, col):
            board.append(col)
            print_nqueens(board)
         if solve_nqueens(board, col + 1):
             return True
         board.pop()
    return False
