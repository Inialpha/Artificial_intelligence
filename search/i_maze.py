import sys
from maze import Maze, StackFrontier, Node


class HeuristicFrontier(StackFrontier):
    """ implement a fontier using the heuristic function """


    def remove(self):
        node = min(((node, node.h_value) for node in self.frontier), key=lambda x: x[1])[0]

        self.frontier.remove(node)
        return node


class Mymaze(Maze):
    """ implements a class to solve a maze"""
    def heuristic_function(self, state):
        """
        Calculate the heuristic function for a maze

        Parameters:
            state (tuple): Current of state maze

        Return:
            int: Estimated cost from the state to the goal
        """

        pos = [s1 - s2 for s1, s2 in zip(state, self.goal)]
        # calculate the Manhattan distance
        pos = min(abs(pos[0]), abs(pos[1]))
        return pos
        
        
    def solve(self):
        """ Find a solution to the maze problem if one exist """

        # create the first node with th start state
        start = Node(state=self.start, parent=None, action=None)
        start.h_value = self.heuristic_function(start.state)
        # initialize a frontier with the staring node
        frontier = HeuristicFrontier()
        frontier.add(start)

        # initialize utility variables to keep track of the nodes and number of nodes explored

        self.explored = set()
        self.num_explored = 0

        # loop until solution is found
        while(True):
            if frontier.empty():
                raise ValueError("No solution found")
            
            node = frontier.remove()
            self.num_explored += 1
            
            # check if solution is found
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # add node to explored
            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    new_node = Node(state=state, action=action, parent=node)
                    new_node.h_value = self.heuristic_function(new_node.state)
                    frontier.add(new_node)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    maze = Mymaze(sys.argv[1])
    maze.print()
    maze.solve()
    print("solving...")
    print("State explored", maze.num_explored)
    maze.print()
    maze.output_image("imaze.png", show_explored=True)
