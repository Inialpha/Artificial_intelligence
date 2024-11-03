import numpy as np

# Constants
X = 1
O = -1
EMPTY = 0

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if np.all(board[i, :] == X) or np.all(board[:, i] == X):
            return X
        elif np.all(board[i, :] == O) or np.all(board[:, i] == O):
            return O
    if np.all(np.diag(board) == X) or np.all(np.diag(np.fliplr(board)) == X):
        return X
    elif np.all(np.diag(board) == O) or np.all(np.diag(np.fliplr(board)) == O):
        return O
    # Check for a tie
    if not np.any(board == EMPTY):
        return 0
    # Game is still ongoing
    return None

def minimax(board, depth, maximizing_player):
    result = evaluate(board)
    print(board)
    if result is not None:
        return result

    if maximizing_player:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = O
                    eval = minimax(board, depth + 1, False)
                    board[i, j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == EMPTY:
                    board[i, j] = O
                    eval = minimax(board, depth + 1, True)
                    board[i, j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = -np.inf
    for i in range(3):
        for j in range(3):
            if board[i, j] == EMPTY:
                board[i, j] = X
                eval = minimax(board, 0, False)
                board[i, j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Example usage
board = np.zeros((3, 3), dtype=int)
print("Initial Board:")
print(board)

# Player X makes the first move
player_X_move = (0, 0)
board[player_X_move] = X
print("After player X's move:")
print(board)

# AI makes the second move
ai_move = find_best_move(board)
board[ai_move] = O
print("After AI's move:")
print(board)

