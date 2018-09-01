# Carole of Mini
A toolset to simulate, solve, and analyze a two-player game on a finite directed acyclic graph (DAG).

The edges of the DAG represent moves in the game. The two players alternate moves from a node to an adjacent node. For a given DAG, the game always begins at the same source node and ends once a sink node is reached. Each sink has a different value. All sink values and paths to the sinks are known to the players at the start of the game. The payoff at the end of the game is the value of the sink on which the game ends.

Player Paul will receive the payoff, so he wants to reach the sink of greatest value. Player Carole will have to pay Paul the payoff, so she wants to reach the sink of least value. They each know the other's objective, and thus account for it in their strategies. Paul will maximize Carole's minimizations of the payoff, and Carole will minimize Paul's maximizations of the payoff.

The main objective of this project is to assess the expected payoff of the game under different conditions.
