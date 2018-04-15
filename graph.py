"@author: Thomas Mason"

from node import *

class Graph:
    def __init__(self, n):
        self.vertices = []
        self.num_leafs = (2 ** n)
        self.num_moves = n
        self.num_nodes = ()(2 ** (n+1))-1)
                
        for i in range(0, self.num_nodes):
            self.vertices.append(Node())
        self.vertices[0].string = "START"
        self.structure()
        

    # Constructor functions
    def structure(self):
        for i in range(0, self.num_leafs-1):
            self.assign_adjacents(s)
    
    
    def assign_adjacents(self, node):
        """Children of node vertices[i] are in:
           vertices[2i + 1]
           vertices[2i + 2] 
        """
        
        index = self.vertices.index(node)
        
        node.adjacents.append(vertices[(2*index)+1])
        node.adjacents.append(vertices[(2*index)+2])
        node.name_adjacents()
    
    
    