"""@author: Thomas Mason"""

class Node:
    def __init__(self, *adjacents):
        self.color = "WHITE"
        self.string = ""
        self.value = None
        self.max = None
        self.min = None
        self.maxchild = None
        self.minchild = None
        self.adjacents = []
