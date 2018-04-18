"""
Algorithm for two-player minimax/maximin game on a DAG.
Player Paul wants to end up at the leaf with the greatest value.
Player Carole has to pay Paul the value of whatever leaf
they end up on, so she wants to end up at the leaf
with the smallest value. One of them gets the first move
at node s, and they alternate moves until ending on a leaf.

DFS-NASH does all the heavy lifting here; once it's done,
the payoff when Paul moves first is stored in MAXIMIN[ROOT] and
the payoff when Carole moves first is stored in MINIMAX[ROOT]

The GAME function simulates the game as it would be played,
but is not necessary to find the payoff (DFS-NASH already
does that). Thus, GAME is just a utility for re-tracing
the path of the game from start to finish, for both potential
first movers.

DFS-NASH is Theta(V + E) and GAME is Theta(V).

@author: Alex Crain
"""
from math import inf


def game(node, mover):
    """Map the path of the game for either first player."""
    if node.minimax is None:
        dfs_nash(node)
    while node.adjacents:
        node, mover = node_selektor(node, mover)
    return node.value


def node_selektor(parent, mover):
    """Decide which node to move to and give the other player the next move."""
    if mover == "PAUL":
        next_mover = "CAROLE"
        child = parent.argmaximin
    elif mover == "CAROLE":
        next_mover = "PAUL"
        child = parent.argminimax
    else:
        raise ValueError('Unknown player ' + mover + ' got a move.')
    return child, next_mover


def dfs_nash(parent):
    """Backward-induct the full game for both potential first movers."""
    parent.max, parent.maximin = -inf, -inf
    parent.min, parent.minimax = inf, inf
    parent.argmaximin = parent
    parent.argminimax = parent
    for child in parent.adjacents:
        dfs_nash(child)
        if parent.max < child.max:
            parent.max = child.max
        if parent.min > child.min:
            parent.min = child.min
        if parent.maximin < child.argminimax.max:
            parent.maximin = child.argminimax.maximin
            parent.argmaximin = child
        if parent.minimax > child.argmaximin.min:
            parent.minimax = child.argmaximin.minimax
            parent.argminimax = child
    if not parent.adjacents:
        parent.max, parent.min = parent.value, parent.value
        parent.maximin, parent.minimax = parent.value, parent.value
