#!/usr/bin/python3
""" a module that creates a node the a node """


class Node:
    """ an implimentation of a node class """

    def __init__(self, parent=None, right=None, left=None, up=None, down=None, state=None):
        """ initialize a Node instance """
        self.parent = parent
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.state = state

    def __str__(self):
        state = str(self.state)

        if self.up:
            up = "\t" + str(self.up.state)
        else:
            up = "\tNone"
        if self.left:
            left = str(self.left.state)
        else:
            left = "None"
        if self.right:
            right = str(self.right.state)
        else:
            right = "None"
        if self.down:
            down = "\t" + str(self.down.state)
        else:
            down = "\tNone"

        return up + "\n" + "          |" + "\n" + left + "---" + state + "---" + right + "\n" + "          |" + "\n" + down + "\n"
        
