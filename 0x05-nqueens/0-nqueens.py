#!/usr/bin/python3
"""
N queens: The N Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append([list(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row+1)
                board[row][col] = 0

    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print_board(solution)
        print()


if __name__ == "__main__":
    main()
