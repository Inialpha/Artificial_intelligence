def util(board, num_moves):
    """ determimes if there is a winner or not """
    size = 3
    X_PLAYER = 1
    O_PLAYER = -1
    
    for player in [X_PLAYER, O_PLAYER]:
        for i in range(size):
            if all(cell == player for cell in board[i]):
                return player
            if all(board[j][i] == player for j in range(size)):
                return player

            if all(board[i][i] == player for i in range(size)) or all(
                    board[i][(size - 1) - i] == player for i in range(size)):
                 return player
    for i in range(size):
        print(board[i][(size - 1) - i])

    print(all(board[i][(size - 1) - i ] == X_PLAYER for i in range(size)))
    if num_moves == 9:
        return 0
    return None

board = [[1, 0, 0],
[0, 0, 0],
[0, 0, 0]]

#print(util(board, 1))

board = [[1, -1, 0],
[0, 0, 0],
[0, 0, 0]]

#print(util(board, 2))

board = [[1, -1, 1],
[0, 0, 0],
[0, 0, 0]]

#print(util(board, 3))

board = [[1, -1, 1],
        [-1, -1, 0],
        [1, 0, -1]]

print(util(board, 7))

board = [[-1, -1, -1],
[1, 1, 0],
[0, 1, 0]]

print(util(board, 6))

board = [[-1, -1, 1],
[-1, 1, 1],
[-1, 1, 0]]

print(util(board, 8))

board = [[-1, 1, 1],
[1, -1, 0],
[0, 0, -1]]

print(util(board, 6))

board = [[1, 1, -1],
[1, -1, 0],
[-1, 0, 11]]

print(util(board, 6))
