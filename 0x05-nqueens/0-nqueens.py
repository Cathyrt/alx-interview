#!/usr/bin/python3
"""
N queens: The N Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
import sys


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - col == i - row or \
           board[i] - col == row - i:
            return False
    return True


def solve_nqueens(N):
    # Check if N is less than 4, which is not allowed for the N Queens problem
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def place_queens(board, row):
        if row == N:
            # All queens have been successfully placed, print the solution
            print([[i, board[i]] for i in range(N)])
        else:
            # Try placing a queen in each column of the current row
            for col in range(N):
                if is_safe(board, row, col):
                    # Queen can be placed at (row, col), update
                    # the board and move to the next row
                    board[row] = col
                    place_queens(board, row + 1)

    # Initialize the board as a list of -1 (no queen placed yet)
    board = [-1] * N
    place_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
