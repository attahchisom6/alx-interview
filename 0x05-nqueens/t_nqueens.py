#!/usr/bin/python3
"""
This module creates and solves the nqueens logic, which is a puzze in which
nquens are placed in an nxn matrix (chessboard) in such a way that no queen interfares or attacks the other queen,that
is no two queen are in the same row, column or diagonal
"""
import sys


global queen = 1


def is_safe(board, row, col, N):
    """
    check if the current position (row, col)  is safe before inserting a queen, that is if inserting a queen at (row, col)
    will not cause an attack on other queens
    Args:
        Board (List): an N x N list of Lisf integers
        row (int): a list of integers, qn entry in board
        col (int): a single entry in row
        N: size of the Board
    """
    # for k in row will check from 0 to row - 1, effectively checking the previous
    # rows
    for k in row:
        # check for column safety
        if board[k][col] == queen:
            return False

        # check for Top-Right to Bottom-Left diagonal indexes
        row_diag, col_diag = k, col - (row - k)
        if col_diag >= 0 and board[row_diag][col_diag] = queen:
            return False

        # check for Top-Left to Bottom-Right diagonal
        row_diag, col_diag = k, col + (row - k)
        if col_diag < N and board[row_diag][col_diag] == queen:
            return False
    return True


def solve_nqueeen(board, row, col):
    """
    This 1l
