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

    def __init__(self, num_moves, distribution="Uniform1", rand_graph=0):
        self.num_moves = num_moves
        self.count_nodes()
        self.vertices = list(Node() for v in range(self.num_nodes))
        if rand_graph == 0:
            self.structure(distribution)
        elif rand_graph == 1:
            self.rand_structure(distribution)
        elif rand_graph == 2:
            self.skip_structure(distribution)

    def count_nodes(self):
        """Derive some useful node tallies from the number of moves."""
        self.num_nodes = (1 << (self.num_moves + 1)) - 1
        self.num_leaves = 1 << self.num_moves
        self.num_parents = (1 << self.num_moves) - 1

    def structure(self, distribution):
        """Assign adjacency lists, strings, and values to each node."""
        for index, vertex in enumerate(self.vertices):
            if index < self.num_parents:
                vertex.adjacents.append(self.vertices[(index << 1) + 1])
                vertex.adjacents.append(self.vertices[(index << 1) + 2])
            else:
                vertex.reset_value(distribution)
            if index < self.num_nodes - 1:
                parent_name = self.vertices[index >> 1].string
                self.vertices[index + 1].string += parent_name + str(index % 2)

    def rand_structure(self, distribution):
        """Structure with random adjacency lists that don't skip a move.
        Note that we may end up with "orphan" nodes this way, which
        would effectively be excluded from the Game.
        """
        for index, vertex in enumerate(self.vertices):
            if index < self.num_parents:
                count = 1 << (index + 1).bit_length()
                choose = randint(1, count)
                adj = choice(self.vertices[count - 1:(count << 1) - 1], choose)
                vertex.assign_adjacents(adj.tolist())
            else:
                vertex.reset_value(distribution)
            if index < self.num_nodes - 1:
                parent_name = self.vertices[index >> 1].string
                self.vertices[index + 1].string += parent_name + str(index % 2)

    def skip_structure(self, distribution):
        """Structure with random adjacency lists that can skip a move.
        Note that we may end up with "orphan" nodes this way, which
        would effectively be excluded from the Game.
        """
        for index, vertex in enumerate(self.vertices):
            if index < self.num_parents:
                start = (1 << (index + 1).bit_length()) - 1
                choose = randint(1, self.num_nodes - start + 1)
                adj = choice(self.vertices[start:], choose)
                vertex.assign_adjacents(adj.tolist())
            else:
                vertex.reset_value(distribution)
            if index < self.num_nodes - 1:
                parent_name = self.vertices[index >> 1].string
                self.vertices[index + 1].string += parent_name + str(index % 2)

    def leaf_values(self):
        """Get the values of all the leaves."""
        return list(v.value for v in self.vertices[self.num_parents:])
