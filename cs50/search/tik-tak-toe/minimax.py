board = [[0 for i in range(3)] for j in range(3)]
EMPTY = 0
x_player = "X"
o_player = "O"
X = 1
O = -1
def util(board):
    # Check horizontal
    i = 0
    j = 0
    if board[i][j] == "X" and board[i][j + 1] == "X" and board[i][j + 2] == "X":
        return 1

    if board[i][j] == "O" and board[i][j + 1] == "O" and board[i][j + 2] == "O":
        return -1

    # Check vertical
    if board[i][j] == "X" and board[i + 1][j] == "X" and board[i + 2][j] == "X":
        return 1

    if board[i][j] == "O" and board[i + 1][j] == "O" and board[i + 2][j] == "O":
        return -1

    # Check diagonals
    if board[i][j] == "X" and board[i + 1][j + 1] == "X" and board[i + 2][j + 2] == "X":
        return 1

    if board[i][j] == "O" and board[i + 1][j + 1] == "O" and board[i + 2][j + 2] == "O":
        return -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY
            return None

    return 0

def terminal(board):
    if util(board) != None:
        return True

def player(board):
    x = 0
    o = 0
    for row in board:
        for col in row:
            if col == "X":
                x += 1
            elif col == "O":
                o += 1
    if 0 == o == x:
        return "X"
    if o > x:
        return "X"
    else:
        return "O"

    return
def minimax(board):

    if terminal(board):
        result = util(board)
        return result

    pl = player(board)
    if player == X:
        max_val = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    val = minimax(board)
                    board[i][j] = EMPTY
                    max_val = max(max_val, val)
        return max_val

    if player == O:
        min_val = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    val = minimax(board)
                    board[i][j] = EMPTY
                    min_val = max(min_val, val)
        return min_val


    state = max(







