WHITE = "W"
BLACK = "B"

EMPTY = None
def init_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if i < (size / 2) - 1 and (i + j) % 2 == 0:
                row.append(BLACK)
            elif i > size / 2 and (i + j) % 2 == 0:
                row.append(WHITE)
            else:
                row.append(EMPTY)
        board.append(row)
    return board

def valid(first, second):
    """def init_board(size):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append((i, j))
            board.append(row)
        return board
    board = init_board(3)
    for row in board:
        print(row)"""
    #print(first, second)
    if (first[0] - 1 == second[0] and first[1] - 1 == second[1]) or (
            first[0] + 1 == second[0] and first[1] + 1 == second[1]) or (
                first[0] - 1 == second[0] and first[1] + 1 == second[1]) or (
                    first[0] + 1 == second[0] and first[1] - 1 == second[1]):
            return True
    return False


"""def init_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append((i, j))
        board.append(row)
    return board
"""
#board = init_board(3)
#for row in board:
#    print(row)
#print(valid((2, 0), (1, 1)))


