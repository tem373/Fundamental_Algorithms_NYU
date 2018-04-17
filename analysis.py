"""
Run some trials of the game and save relevant parameters
for analysis.


@author: Alex Crain, Thomas Mason
"""
from graph import *
from node import *

def enum_graph_structure(graph):
    """Uses graphviz program to create a .gv file (must be compiled separately)
    to illustrate the structure of the tree. Mostly created to help keep track 
    of large trees."""

    filepath = "graph_structure.gv"
    filestring = "digraph {\n"

    string_fragment = ""

    # Run through vertices
    for node in graph.vertices:
        # Parent nodes
        if node.adjacents:
            child1 = node.adjacents[0]
            child2 = node.adjacents[1]
            frag1 = ""
            frag2 = ""
            
            if child1.value:
                frag1 = "\t{} -> {}[label=\"{}\"];\n".format(node.string, child1.string, '%.2f' % child1.value)
                frag2 = "\t{} -> {}[label=\"{}\"];\n".format(node.string, child2.string, '%.2f' % child2.value)                
            
            elif not child1.value:
                frag1 = "\t{} -> {};\n".format(node.string, child1.string)
                frag2 = "\t{} -> {};\n".format(node.string, child2.string)
            string_fragment = string_fragment + frag1 + frag2
            
    
    # Write the filestring into the file    
    filestring = filestring + string_fragment + '}\n'

    with open(filepath, 'w') as outfile:
        outfile.write(filestring)

    # To run the file
    print("To generate the graph in .png format, run: ")
    print("dot -Tpng -O graph_structure.gv")

class Trial:
    """Holds parameters and results of one run of the game."""
    def __init__(self, id_number, first_player, last_player):
        self.id_number = -1
        self.first_move = self.was_player_paul(first_player)
        self.last_move = self.was_player_paul(last_player)
        
    def was_player_paul(self, player):
        was_paul = False
        if player == "PAUL":
            was_paul = True
        elif player == "CAROLE":
            was_paul = False
        else:
            raise ValueError('Unknown player ' + player + ' got a move.')
        return was_paul
