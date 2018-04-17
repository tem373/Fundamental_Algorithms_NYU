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
    """Checks to see if the player provided a legitimate player (Paul or Carole)"""
    if (player1 not in ["PAUL", "CAROLE"]):
        raise argparse.ArgumentTypeError("Player must be either PAUL or CAROLE")
    return player1

parser = argparse.ArgumentParser(description="Graph Theory Game")
optional_args = parser._action_groups.pop()

# Define required arguments
required_args = parser.add_argument_group("Required Arguments: ")
# Give the number of moves for the game (ex: 3 == Paul->Carole->Paul)
required_args.add_argument('--moves', dest='moves', type=int,
    help='How many moves (n) are in the game?', required=True)
# Give how many games of the same type (but different values) you want to run
# (ex: 5 == play 5 games with <n> moves and player1 = <your choice>)
required_args.add_argument('--iterations', dest='iterations', type=int,
    help='How many samples of the specified game to run', required=True)

# Specify who you want to play first
optional_args.add_argument('--player1', dest='player1', type=check_player,
    help='Give either /"PAUL/" or /"CAROLE/" as the first player',
    required=False, default="PAUL")
parser._action_groups.append(optional_args)

args = parser.parse_args()
print(args)

# Defining the provided user input as regular variables
moves = args.moves
iterations = args.iterations
player1 = str(args.player1)

################################################################################
#                                  Setup and Run                               #
################################################################################

graph = Graph(moves)
enum_graph_structure(graph, player1)

payoff = game(graph.vertices[0], player1)
print("Payoff: " + str(payoff))

