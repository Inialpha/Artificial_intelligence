"""
Tic Tac Toe Player
"""

import math

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
    actions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.append(board[i][j])
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if board[row][col] != EMPTY:
        raise Exception
    b = board.deepcopy()
    try:
        b[row][col] = player(board)
    except IndexError:
        raise IndexError
    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    i = 0
    j = 0
    for player in [X, O]:
        if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player:
            return player

        if board[i + 1][j] == player and board[i + 1][j + 1] == player and board[i + 1][j + 2] == player:
            return player

        if board[i + 2][j] == player and board[i + 2][j + 1] == player and board[i + 2][j + 2] == player:
            return player

        # check horizontal
        # colum 0
        if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player:
            return player

        # colum 1
        if board[i][j + 1] == player and board[i + 1][j + 1] == player and board[i + 2][j + 1] == player:
            return player
        
        # colum 2

        if board[i][j + 2] == player and board[i + 1][j + 2] == player and board[i + 2][j + 2] == player:
            return player

        # check diagonals
        if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player:
            return player

        if board[i][j + 2] == player and board[i + 1][j + 1] == player and board[i + 2][j] == player:
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) is not None:
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

    if utility(board) == X:
        return 1
    if utility(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    actions = actions(board)
    min_val = float('inf')
    for actions in actions:
        board = result(action, board)
        val = minimax(board)
        r, c = action
        board[r][c] = EMPTY
        min_val = min(min_val, val)
    return min_val


