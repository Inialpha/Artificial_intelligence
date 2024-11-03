#!/usr/bin/python3
""" a module that implements a tree """
from node import Node


class Board:
    """ a function implimenting the dfs algorithm """

    def __init__(self, size=0):
        self.size = size
        self.root = None

    def create(self):


        created = []

        self.root = Node(state=(0, 0))
        queue = [self.root]
        created.append(self.root.state)
        node = self.root
        while node.state <= (self.size, self.size):
            if not queue:
                return
            node = queue.pop(0)
            row, col = node.state

            directions = (
                ("right", (row, col + 1)),
                ("left", (row, col - 1)),
                ("up", (row - 1, col)),
                ("down", (row + 1, col))
            )


            for direction, state in directions:
                if 0 <= state[0] < self.size and 0 <= state[1] < self.size:
                    if state not in created:
                        new_node = Node(state=state)
                        queue.append(new_node)
                        created.append(new_node.state)
                        setattr(node, direction, new_node)
                    if node.up:
                        node.right = node.up.right.down if node.up.right else node.up.right
                    if node.right:
                        node.right.left = node
                    if direction == 'right':
                        setattr(new_node, "left", node)
                    if direction == 'down':
                        setattr(new_node, "up", node)

    
    def print(self):
        line = self.root
        node = line
        for i in range(self.size ** 2):
            print(node.state, end="")
            node = node.right
            if (i + 1) % self.size == 0:
                node = line.down
                line = node
                print()


        

board = Board(4)
board.create()
board.print()
