"""
Constructs a graph to the Game's specifications:
The starting node's string's empty, all other nodes'
strings encode a unique sequence of moves,
and all nodes save the leaves receive adjacencies.

@author: Thomas Mason, Alex Crain
"""
from random import uniform
from node import Node

class Graph:
    """Construct the DAG for an n-move Game."""
    def __init__(self, num_moves):
        self.num_moves = num_moves
        self.count_nodes()
        self.vertices = list(Node() for v in range(self.num_nodes))
        self.structure()


    def count_nodes(self):
        """Derive some useful node tallies from the number of moves."""
        self.num_nodes = 2 ** (self.num_moves + 1) - 1
        self.num_leaves = 2 ** self.num_moves
        self.num_parents = 2 ** self.num_moves - 1


    def structure(self):
        """Assign adjacency lists and strings to each node."""
        for index, vertex in enumerate(self.vertices):
            if index < self.num_parents:
                vertex.adjacents.append(self.vertices[2 * index + 1])
                vertex.adjacents.append(self.vertices[2 * index + 2])
            else:
                vertex.value = uniform(-1, 1)
            if index < self.num_nodes - 1:
                parent_name = self.vertices[int(index / 2)].string
                self.vertices[index + 1].string += parent_name + str(index % 2)


    def leaf_values(self):
        """Get the values of all the leaves."""
        return list(v.value for v in self.vertices[self.num_parents:])
