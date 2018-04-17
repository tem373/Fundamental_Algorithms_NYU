"@author: Thomas Mason"

import argparse

from algorithm import *
from graph import *
from node import *
from analysis import *

################################################################################
#                                 Argparse Setup                               #
################################################################################
def check_player(player1):
    if (player1 not in ["PAUL", "CAROLE"]):
        raise argparse.ArgumentTypeError("Player must be either PAUL or CAROLE")

parser = argparse.ArgumentParser(description="Graph Theory Game")
optional_args = parser._action_groups.pop()

required_args = parser.add_argument_group("Required Arguments: ")
required_args.add_argument('--moves', dest='moves', type=int,
    help='How many moves (n) are in the game?', required=True)
required_args.add_argument('--iterations', dest='iterations', type=int,
    help='How many samples of the specified game to run', required=True)
    
optional_args.add_argument('--player1', dest='player1', type=check_player,
    help='Give either /"PAUL/" or /"CAROLE/" as the first player',
    required=False, default='PAUL')
parser._action_groups.append(optional_args)

args = parser.parse_args()
print(args)


################################################################################
#                                  Setup and Run                               #
################################################################################

graph = Graph(args.moves)
enum_graph_structure(graph)

payoff = game(graph.vertices[0], args.player1)
print("Payoff: " + str(payoff))

