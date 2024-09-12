#!/usr/bin/python3
"""Solve the n queens puzzle"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif sys.argv[1].isdigit() is False:
    print("N must be a number")
    sys.exit(1)
elif int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
N = int(sys.argv[1])


def solve_n_queens(n):
    """Solve the N queens problem for n x n chess board

    Args:
        n (int): The number of queens
    """
    board = [[0] * n for _ in range(n)]
    pos_diag = set()
    neg_diag = set()
    cols = set()

    def backtrack(r):
        """Perform the backtracking on row r
        """
        if (r == n):
            res = []
            [[res.append(c) for c in r if c] for r in board]
            print(res)
            return
        for c in range(n):
            if (c in cols or (r - c) in pos_diag
                    or (r + c) in neg_diag):
                continue

            board[r][c] = [r, c]
            pos_diag.add(r - c)
            neg_diag.add(r + c)
            cols.add(c)
            backtrack(r + 1)
            pos_diag.remove(r - c)
            neg_diag.remove(r + c)
            cols.remove(c)
            board[r][c] = 0
        return
    backtrack(0)


solve_n_queens(N)
