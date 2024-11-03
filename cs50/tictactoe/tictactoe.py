"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                 o += 1
    return X if x < o else O if o < x else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    my_actions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                my_actions.append((i, j))
    return my_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if board[row][col] != EMPTY:
        raise Exception
    b = copy.deepcopy(board)
    try:
        b[row][col] = player(board)
    except IndexError:
        raise IndexError
    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board_len = len(board[0])
    for player in [X, O]:
        for i in range(len(board)):
            if all(col == player for col in board[i]):
                return player

            if all(board[j][i] == player for j in range(board_len)):
                return player

        if all(board[i][i] == player for i in range(board_len)) or all(board[i][(board_len -1) - i] == player for i in range(board_len)):
                return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) :
        return True

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def max_value(board):
    """
    Returns the value of the maximum move for the maximizing player.
    """
    if terminal(board):
        return utility(board)

    new_actions = actions(board)
    val = float("-inf")
    for action in new_actions:
        new_board = result(board, action)
        val = max(val, min_value(new_board))
    return val

def min_value(board):
    """
    Returns the value of the minimum move for the minimizing player.
    """
    if terminal(board):
        return utility(board)

    new_actions = actions(board)
    val = float("inf")
    for action in new_actions:
        new_board = result(board, action)
        val = min(val, max_value(new_board))
    return val


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "O": 
        my_actions = actions(board)
        min_val = float('inf')
        best_move = None
        for action in my_actions:
            new_board = result(board, action)
            val = max_value(new_board)
            if val < min_val:
                min_val = val
                best_move = action 
        return best_move

    if player(board) == "X":
        my_actions = actions(board)
        max_val = float('-inf')
        best_move = None
        for action in my_actions:
            new_board = result(board, action)
            val = min_value(new_board)
            if val > max_val:
                max_val = val
                best_move = action
        return best_move
