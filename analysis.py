"""
Graph visualization utility.
Might add other plotting tools here later.
@author: Thomas Mason
"""
from graph import *
from node import *


def enum_graph_structure(graph, player1):
    """Uses graphviz program to create a .gv file (must be compiled separately)
    to illustrate the structure of the tree. Mostly created to help keep track 
    of large trees."""

    filepath = "graph_structure.gv"
    filestring = "digraph {\n \tforcelabels=true;\n"

    string_fragment = ""
    player = player1
    player_colors = {"PAUL": "red", "CAROLE": "blue"}

    # Run through vertices
    for node in graph.vertices:

        # Parent nodes
        if node.adjacents:
            child1 = node.adjacents[0]
            child2 = node.adjacents[1]
            frag1 = ""
            frag2 = ""

            if child1.value:
                nodestr1 = "\t{} [label=\"{}, {}\"];\n".format(
                    child1.string, child1.string, " %.2f" % child1.value)
                nodestr2 = "\t{} [label=\"{}, {}\"];\n".format(
                    child2.string, child2.string, " %.2f" % child2.value)

                frag1 = "\t{} -> {};\n".format(node.string, child1.string)
                frag2 = "\t{} -> {};\n".format(node.string, child2.string)

            elif not child1.value:
                nodestr1 = ""
                nodestr2 = ""
                frag1 = "\t{} -> {};\n".format(node.string, child1.string)
                frag2 = "\t{} -> {};\n".format(node.string, child2.string)
            string_fragment = string_fragment + nodestr1 + nodestr2 + frag1 + frag2

            # Flip players
            if (player == "PAUL"):
                player = "CAROLE"
            elif (player == "CAROLE"):
                player = "PAUL"

    # Write the filestring into the file
    filestring = filestring + string_fragment + '}\n'

    with open(filepath, 'w') as outfile:
        outfile.write(filestring)

    # To run the file
    print("To generate the graph in .eps format, run: ")
    print("dot -Teps graph_structure.gv -o graph_structure.eps")

class Trial:
    """Holds parameters and results of one run of the game."""
    def __init__(self, num_id, num_moves, first_player, payoff):
        self.num_id = -1
        self.num_moves = num_moves
        self.first_player = first_player
        self.set_last_player(first_player, num_moves)
        self.payoff = payoff

print("dot -Tpng -O graph_structure.gv")
