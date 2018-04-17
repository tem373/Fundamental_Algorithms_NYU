"""
Algorithm for two-player minimax game on a DAG.
Player Paul wants to end up at the leaf with the greatest value.
Player Carole has to pay Paul the value of whatever leaf
they end up on, so she wants to end up at the leaf
with the smallest value. One of them gets the first move
at node s, and they alternate moves until ending on a leaf.


@author: Alex Crain
"""


def game(node, mover):
    """Play the game and return Paul's payoff."""
    if node.min is None or node.max is None:
        dfs_extrema(node)
    while node.adjacents:
        node, mover = node_selektor(node, mover)
    return node.value


def node_selektor(parent, mover):
    """Decide which node to move to and give the other player the next move."""
    child = None
    next_mover = None
    if mover == "PAUL":
        next_mover = "CAROLE"
        child = parent.argmaximin
    elif mover == "CAROLE":
        next_mover = "PAUL"
        child = parent.argminimax
    else:
        raise ValueError('Unknown player ' + mover + ' got a move.')
    return child, next_mover


def dfs_extrema(parent):
    """Endow each node in a DAG with the max and min of its children."""
    value_min = float("inf")
    value_max = float("-inf")
    value_minimax = float("inf")
    value_maximin = float("-inf")
    parent.color = "GRAY"
    for child in parent.adjacents:
        if child.color == "WHITE":
            dfs_extrema(child)
            if value_min >= child.min:
                value_min = child.min
            if value_maximin < child.argminimax.max:
                value_maximin = child.argminimax.maximin
                argmaximin = child
            if value_max < child.max:
                value_max = child.max
            if value_minimax >= child.argmaximin.min:
                value_minimax = child.argmaximin.minimax
                argminimax = child
    parent.color = "BLACK"
    if parent.adjacents:
        parent.min = value_min
        parent.max = value_max
        parent.minimax = value_minimax
        parent.maximin = value_maximin
        parent.argminimax = argminimax
        parent.argmaximin = argmaximin
    else:
        parent.min = parent.value
        parent.max = parent.value
        parent.minimax = parent.value
        parent.maximin = parent.value
        parent.argminimax = parent
        parent.argmaximin = parent
