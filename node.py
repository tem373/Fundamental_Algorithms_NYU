"@author: Thomas Mason"

import random

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
        
        # Non-leaf nodes
        if (len(adjacents) != 0):
            for node in adjacents:
                self.adjacents.append(node)
            #name_adjacents()     #maybe dont need here

        # Leaf nodes
        elif (len(adjacents) == 0):
            self.value = random.uniform(-1, 0)
        
    def name_adjacents(self):
        if(len(adjacents) != 0):
            adjacents[0].string = self.string + '0'
            adjacents[1].string = self.string + '1'