# Source:   https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
# Problem:  find a way to place n queens on an n x n board S.T. no two
#           queens are attacking each other
# Goal:     find all possible soln's and quickly
#           use effective backtracking algorithm

import numpy as np

# recursive function that backtracks to find all possible solns\
# in a class this method would be private
def recursive_place_queens(n, row, board, result):
    # Base case
    if row==n:
        result.append(board)
    # Recursive Case
    else:
        for col in range(n):
            board[row] = col
            if is_valid(board):
                recursive_place_queens(n, row+1, board, result)

def place_n_queens(n):
    board = np.zeros(n)
    result = np.empty((0,n))
    recursive_place_queens(n, 0, board, result)
    to_file(board)

def is_valid(board):
    pass

def to_file(output):
    pass
