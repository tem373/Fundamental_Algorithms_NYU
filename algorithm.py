"""
Algorithm for two-player minimax/maximin game on a DAG.
Player Paul wants to end up at the leaf with the greatest value.
Player Carole has to pay Paul the value of whatever leaf
they end up on, so she wants to end up at the leaf
with the smallest value. One of them gets the first move
at ROOT, and they alternate moves until ending on a leaf.

They each know the other's strategy, and thus account for it
in their own. Paul will perfectly maximize Carole's minimizations
of the payoff, and Carole of Delphi will perfectly minimize
Paul's maximizations of the payoff.

DFS-NASH does all the heavy lifting here; once it's done,
the payoff when Carole moves first is stored in MINIMAX[ROOT],
and the payoff when Paul moves first is stored in MAXIMIN[ROOT].

The GAME function steps through all optimal moves of the game,
but is not necessary to find the payoff (DFS-NASH already
does that). Thus, GAME is just a utility for re-tracing
the optimal path of the game from start to finish,
for each potential first mover.

@author: Alex J. Crain
"""
from math import inf


def dfs_nash(parent):
    """Backward-induct the full game for both starting players."""
    parent.minimax, parent.maximin = inf, -inf
    for child in parent.adjacents:
        dfs_nash(child)
        if parent.minimax > child.maximin:
            parent.minimax = child.maximin
        if parent.maximin < child.minimax:
            parent.maximin = child.minimax
    if not parent.adjacents:
        parent.minimax, parent.maximin = parent.value, parent.value


def game(node, mover):
    """Map the path of the game for either first player."""
    if node.argminimax is None or node.argmaximin is None:
        dfs_nash_paths(node)
    while node.adjacents:
        node, mover = node_selektor(node, mover)
    return node.value


def node_selektor(parent, mover):
    """Decide to which node this player will move, and alternate players."""
    if mover == "CAROLE":
        child = parent.argminimax
        next_mover = "PAUL"
    elif mover == "PAUL":
        child = parent.argmaximin
        next_mover = "CAROLE"
    else:
        raise ValueError('Unknown player ' + mover + ' got a move.')
    return child, next_mover


def dfs_nash_paths(parent):
    """DFS-NASH with an extra step to store the moves made at each node."""
    parent.minimax, parent.maximin = inf, -inf
    for child in parent.adjacents:
        dfs_nash_paths(child)
        if parent.minimax > child.maximin:
            parent.minimax = child.maximin
            parent.argminimax = child
        if parent.maximin < child.minimax:
            parent.maximin = child.minimax
            parent.argmaximin = child
    if not parent.adjacents:
        parent.minimax, parent.maximin = parent.value, parent.value
