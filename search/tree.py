#!/usr/bin/python3
""" a module that implements a tree """
class Node:
    def __init__(self, value=None, parent=None, right=None, left=None):
        self._value = value
        self.parent = parent
        self.right = right
        self.left = left

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError("value must be a number")
        self._value = value


class Tree:
    """ a function implimenting the dfs algorithm """

    def __init__(self, values=None):
        self.values = values

    def create(self):
        frontier = []
        self.root = Node(self.values[0])
        print(self.root.value)
        frontier.append(self.root)
        for i, value in enumerate(self.values[1:]):
            print(self.values, value)
            node = frontier.pop(0)
            new_node = Node(value)
            print(new_node.value)
            new_node.parent = node
            if i % 2 != 0:
                node.left = new_node
            else:
                node.right = new_node
            frontier.append(new_node)

    def depth(self):
        node = self.root
        def d(node):
            if node is None:
                return 0
            
            left_depth = d(node.left)
            right_depth = d(node.right)
            return max(left_depth, right_depth) + 1
        return d(node)


    def print(self):

        def p(root, level=0, left=0, right=0, prefix="."):
            if root:
                is_left = root.parent and root.parent.left == root
                if is_left:
                    print(" " * (left * 5) + prefix + "---" + f"({root.value})" + "---" + prefix)
                else:
                    print(" " * (right * 5) + prefix + "---" + f"({root.value})" + "---" + prefix)
                p(root.left, level + 1, left - 1, right, prefix)
                p(root.right, level + 1, left, right + 1, prefix)

        depth = self.depth()
        level = depth // 2
        p(self.root, level, left=level, right=level)
            

    
l = [1, 2, 3, 4, 5, 6, 7, 8]
tree = Tree(l)
tree.create()
tree.print()
