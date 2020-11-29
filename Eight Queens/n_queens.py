# Source:   https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
# Problem:  find a way to place n queens on an n x n board S.T. no two
#           queens are attacking each other
# Goal:     find all possible soln's and quickly
#           use effective backtracking algorithm

from PIL import Image, ImageDraw
import numpy as np

# TODO: check if dir exists and if not create it
DIR = 'Eight Queens/Solutions'
DIM = 600

# recursive function that backtracks to find all possible solns\
# in a class this method would be private
# @postcondition: result will contain all soln's
def recursive_place_queens(n, row, board, result):
    # Base case
    if row==n:
        result.append(board)
    # Recursive Case
    else:
        for col in range(n):
            board = np.append(board, col)
            if is_valid(board, n):
                recursive_place_queens(n, row + 1, board, result)
            board = np.delete(board, -1)


# public method to begin recursive search for solutions
# only requires one parameter, n
def place_n_queens(n):
    board = np.empty(0, int)
    solns = []
    recursive_place_queens(n, 0, board, solns)
    # remove_variations(solns, n)
    draw_solns(solns, n)


# remove soln's that are rotations/reflections
# of one another
# TODO
def remove_variations(solns, n):
    
    for i in range(len(solns)):
        try:
            var = []
            board = solns[i].copy()
            temp = solns[i].copy()
        except IndexError:
            break

        # Rotations
        for _ in range(3):
            temp = rotate(temp)
            if (temp!=board).all():
                board = temp.copy()
                var.append(board)

        # Reflections:
        board = solns[i].copy()
        temp = reflect(solns[i])
        if (temp!=board).all():
            board = temp.copy()
            var.append(board)
        for _ in range(3):
            temp = rotate(temp)
            if (temp!=board).all():
                board = temp.copy()
                var.append(board)

        # remove variations
        for v in range(len(var)):
            for s in range(len(solns[i:])):
                if (solns[s]==var[v]).all():
                    solns.pop(s)
                    break


def rotate(board):
    n = len(board)
    result = np.zeros(n, int)
    for i in range(n):
        row = int(board[i])
        col = (n-1) - i
        result[row] = col
    return result


def reflect(board):
    return np.flip(board)


# our algorithm naturally asserts that queens occupy different rows
# this method additionally checks that they occupy different columns
# and diagonals
# @return: returns a boolean
def is_valid(board, n):
    m = len(board)

    # check columns
    if len(np.unique(board)) != m:
        return False

    # check diagonals
    d_1 = np.zeros(m)
    d_2 = np.zeros(m)
    for i in range(m):
        col = board[i]
        row = i
        d_1[i] = col - row
        d_2[i] = col + row - (n-1)
    if len(np.unique(d_1)) != m:
        return False
    if len(np.unique(d_2)) != m:
        return False
    return True


def draw_chess_board(draw, n):
    color = ['bisque', 'saddlebrown']
    switch = lambda x : (x + 1) % 2
    c = 0
    size = DIM/n
    for x in range(n):
        x0 = x * size
        x1 = x0 + size
        for y in range(n):
            y0 = y * size
            y1 = y0 + size
            draw.rectangle(
                (x0,y0,x1,y1),
                fill=color[c],
                outline='coral'
                )
            c = switch(c)
        if n % 2 == 0:
            c = switch(c)


def draw_queen(draw, unit, x0, y0):
    crown = [
        (2.5, 5),
        (1, 2),
        (3, 3.5),
        (4, 1),
        (5, 3.5),
        (7, 2),
        (5.5, 5)
    ]
    body = [
        (2, 7),
        (2.5, 5.5),
        (5.5, 5.5),
        (6, 7)
    ]
    for i in range(len(crown)):
        j = i - (len(crown) - 1)
        x1 = x0 + crown[i][0] * unit
        y1 = y0 + crown[i][1] * unit
        x2 = x0 + crown[j][0] * unit
        y2 = y0 + crown[j][1] * unit
        draw.line([(x1,y1),(x2,y2)], fill='black', width=4)
    for i in range(len(body)):
        j = i - (len(body) - 1)
        x1 = x0 + body[i][0] * unit
        y1 = y0 + body[i][1] * unit
        x2 = x0 + body[j][0] * unit
        y2 = y0 + body[j][1] * unit
        draw.line([(x1,y1),(x2,y2)], fill='black', width=4)


# draw chessboard representation of solutions
# make file for each soln s in the format n_s.jpg
def draw_solns(solns, n):
    size = DIM/n
    for s in range(len(solns)):
        im = Image.new('RGB', (DIM, DIM))
        draw = ImageDraw.Draw(im)
        draw_chess_board(draw, n)
        for i in range(n):
            x0 = size * solns[s][i]
            y0 = size * i
            unit = (DIM/n)/8
            draw_queen(draw, unit, x0, y0) 
        # save image
        filename = DIR + '/' + str(n) + '_' + str(s) + '.jpg'
        im.save(filename, quality=95)


if __name__ == "__main__":
    place_n_queens(5)