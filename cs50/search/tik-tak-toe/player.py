""" module for player class """


class Player:
    """ implements a player """

    def action(self, state):
        """ return all posible action for the state """

    def result(self, state, action):
        """ return the result for the action """

    def terminal(self):
        """ determines if game is over """

    def play(self, state):
        """ the play method """

        while True;
            if self.terminal():
                return state

            state = min(self.result(state, action))
