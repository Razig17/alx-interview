#!/usr/bin/python3
"""Solve the N queens puzzle."""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
elif int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

N = int(sys.argv[1])


def solve_n_queens(n):
    """Solve the N queens problem for n x n chess board.

    Args:
        n (int): The number of queens.
    """
    board = [[0] * n for _ in range(n)]
    pos_diag = set()
    neg_diag = set()
    cols = set()

    def backtrack(row):
        """Perform backtracking to find solutions.

        Args:
            row (int): The current row being explored.
        """
        if row == n:
            result = []
            [[result.append(c) for c in r if c] for r in board]
            print(result)
            return

        for col in range(n):
            if col in cols or (row - col) in pos_diag\
                    or (row + col) in neg_diag:
                continue

            board[row][col] = [row, col]
            pos_diag.add(row - col)
            neg_diag.add(row + col)
            cols.add(col)

            backtrack(row + 1)

            board[row][col] = 0
            pos_diag.remove(row - col)
            neg_diag.remove(row + col)
            cols.remove(col)

    backtrack(0)


solve_n_queens(N)
