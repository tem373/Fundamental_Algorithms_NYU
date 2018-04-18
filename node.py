"""
Basic node class with a few special fields for the Game
(maximin, minimax, random value assignment, et cetera).

@author: Thomas Mason, Alex Crain
"""
from random import uniform


class Node:
    """A node representing one stage of the Game."""

    def __init__(self, distribution=None, adjacents=None):
        self.string = ""
        self.reset_value(distribution)
        self.maximin = None
        self.minimax = None
        self.argmaximin = None
        self.argminimax = None
        self.assign_adjacents(adjacents)

    def assign_adjacents(self, adjacents):
        """Assign adjacency list."""
        self.adjacents = list()
        if adjacents is not None:
            self.adjacents = list(a for a in adjacents)

    def reset_value(self, distribution=None):
        """Pull a node value from a specified distribution."""
        self.value = None
        if distribution is not None:
            bound = int(distribution[-1])
            lower, upper = -bound, bound
            key = distribution[:-1]
            if key == "Uniform":
                self.value = uniform(lower, upper)
            else:
                raise ValueError(
                    'Unknown distribution ' + str(distribution) + '.')
