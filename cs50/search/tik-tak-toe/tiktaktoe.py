""" a tik tak toe game """

from time import sleep

class TikTakToe:
    """ implementation of a tak toe game """

    EMPTY = 0
    X_PLAYER = 1
    O_PLAYER = -1

    def __init__(self):
        """ initialize the class """
        self.size = 3
        self.board = [[0 for i in range(self.size)] for j in range(self.size)]
        self.stages = []
        self.num_moves = 0

    def actions(self):
        """ return all posible action for the state """
        actions = []
        #print()
        #self.print()
        #sleep(1)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.EMPTY:
                    actions.append((i, j))
        return actions



    def result(self, action, player):
        """ return the result for the action """
        row, col = action
        self.board[row][col] = player


    def player(self):
        """ returns the player to play """
        x_count = 0
        o_count = 0

        for row in self.board:
            for col in row:
                if col == self.X_PLAYER:
                    x_count += 1
                elif col == self.O_PLAYER:
                    o_count += 1
        return self.O_PLAYER if o_count < x_count else self.X_PLAYER if x_count < o_count else self.X_PLAYER



    def util(self):
        """ determimes if there is a winner or not """
        for player in [self.X_PLAYER, self.O_PLAYER]:
            for i in range(self.size):
                if all(cell == player for cell in self.board[i]):
                    return player
                if all(self.board[j][i] == player for j in range(self.size)):
                    return player

            if all(self.board[i][i] == player for i in range(self.size)) or all(
                    self.board[i][(self.size - 1) - i] == player for i in range(self.size)):
                 return player
        if all(col != self.EMPTY for row in self.board for col in row):
            return 0
        return None

    def terminal(self):
        """ determines if game is over """
        return self.util() is not None
    

    def print(self):
        for row in self.board:
            print(row)

    def solve(self):
        """ play the game """
        print("solving...")

        while True:

            """ loop until the game is over """

            if self.terminal():
                result = self.util()
                return result
            self.stages.append(self.board)

            player = self.player()
            self.print()
            print("Stage: {} --- Player: {}".format(self.num_moves, player))
            self.num_moves += 1
            self.result(self.minimax(), player)
          
    def minimax(self):
        player = self.player()
        if player == self.X_PLAYER:
            best_move = None
            best_val = float('-inf')
            values = []
            actions = self.actions()
            for action in actions:
                self.result(action, self.X_PLAYER)
                val = self.o_player()
                self.result(action, self.EMPTY)
                values.append((action, val))
                if val > best_val:
                    best_val = val
                    best_move = action
            print(values)
            return best_move

        elif player == self.O_PLAYER:
            best_move = None
            best_val = float('inf')
            values = []
            actions = self.actions()
            for action in actions:
                self.result(action, self.O_PLAYER)
                val = self.x_player()
                self.result(action, self.EMPTY)
                values.append((action, val))
                if val < best_val:
                    best_val = val
                    best_move = action
            print(values)
            return best_move


    def x_player(self):

        # initialize the max_val negetive infinity
        if self.terminal():
            return self.util()

        max_val = float('-inf')
        actions = self.actions()
        for action in actions:
            self.result(action, self.X_PLAYER)
            val = self.o_player()
            # backtrack
            self.result(action, self.EMPTY)
            max_val = max(max_val, val)
        return max_val

    def o_player(self):
        if self.terminal():
            return self.util()

        min_val = float('inf')
        actions = self.actions()
        for action in actions:
            self.result(action, self.O_PLAYER)
            val = self.x_player()
            self.result(action, self.EMPTY)
            min_val = min(min_val, val)
        return min_val




            
t = TikTakToe()
t.print()
winner = t.solve()
t.print()
print(winner)
