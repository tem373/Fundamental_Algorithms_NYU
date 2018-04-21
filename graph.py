"""
Constructs a graph to the Game's specifications:
The starting node's string's empty, all other nodes'
strings encode a unique sequence of moves,
and all nodes save the leaves receive adjacencies.

@author: Thomas Mason, Alex Crain
"""
from random import randint
from numpy.random import choice
from node import Node


class Graph:
    """Construct the DAG for an n-move Game."""

    def __init__(self, num_moves, distribution="Uniform1", graph_mode=0):
        self.num_moves = num_moves
        self.count_nodes()
        self.vertices = list(Node() for v in range(self.num_nodes))
        self.structure(distribution, graph_mode)

    def count_nodes(self):
        """Derive some useful node tallies from the number of moves."""
        self.num_nodes = (1 << (self.num_moves + 1)) - 1
        self.num_leaves = 1 << self.num_moves
        self.num_parents = (1 << self.num_moves) - 1

    def structure(self, distribution, graph_mode):
        """Assign adjacency lists, strings, and values to each node."""
        for index, vertex in enumerate(self.vertices):
            if index < self.num_parents:
                vertex.adjacents = self.define_adjacents(index, graph_mode)
            else:
                vertex.reset_value(distribution)
            if index < self.num_nodes - 1:
                parent_name = self.vertices[index >> 1].string
                self.vertices[index + 1].string += parent_name + str(index % 2)
        self.vertices[0].string = 'START'

    def define_adjacents(self, index, graph_mode):
        """Assign deterministic (tree-structured) or random adjacency lists.
        Random mode 1 does not skip moves, whereas random mode 2 can.
        Note that we may end up with "orphan" nodes in the random cases,
        which will effectively be excluded from the Game."""
        if graph_mode == 0:
            adj = list()
            adj.append(self.vertices[(index << 1) + 1])
            adj.append(self.vertices[(index << 1) + 2])
        elif graph_mode == 1:
            count = 1 << (index + 1).bit_length()
            num_choose = randint(1, count)
            adj = choice(self.vertices[count - 1:(count << 1) - 1], num_choose)
            adj = adj.tolist()
        elif graph_mode == 2:
            start = (1 << (index + 1).bit_length()) - 1
            num_choose = randint(1, self.num_nodes - start + 1)
            adj = choice(self.vertices[start:], num_choose)
            adj = adj.tolist()
        else:
            raise ValueError('Unknown graph mode ' + graph_mode)
        return adj

    def leaf_values(self):
        """Get the values of all the leaves."""
        return list(v.value for v in self.vertices[self.num_parents:])
