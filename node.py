"""@author: Thomas Mason"""
from random import uniform


class Node:
    """A node representing one stage of the Game."""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, give_value=None, color="WHITE", adjacents=None):
        self.color = color
        self.string = ""
        self.reset_value(give_value)
        self.max = None
        self.min = None
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

    def reset_value(self, give_value):
        """Pull a node value from a specified distribution."""
        self.value = None
        if give_value is not None:
            if give_value == "Uniform":
                self.value = uniform(-1, 1)
            else:
                raise ValueError('Unknown distribution ' + str(give_value) + '.')
