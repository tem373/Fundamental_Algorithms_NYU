"""
Algorithm for two-player minimax game on a DAG.
Starting from some node s, Player Paul wants to
end up at the leaf with the greatest value. Player
Carole has to pay Paul the value of whatever leaf
they end up on, so she wants to end up at the
leaf with the smallest value.


@author: Alex Crain
"""

def game(node_start, first_mover):
    """Play the game and return Paul's payoff."""
    if node_start.min is None:
        depth_first_minmax(node_start)
    mover = first_mover
    node_current = node_start
    while (node_current.adjacents) != 0:
        node_current, mover = node_selektor(node_current, mover)
    return node_current.value

def node_selektor(parent, mover):
    """Decide which node to move to and give the other player the next move."""
    child = None
    if mover == "PAUL":
        child = parent.maxchild
        mover = "CAROLE"
    elif mover == "CAROLE":
        child = parent.minchild
        mover = "PAUL"
    return child, mover

def depth_first_minmax(parent):
    """Endow each node in a DAG with the max and min of its children."""
    value_min = float("inf")
    value_max = float("-inf")
    for child in parent.adjacents:
        if child.color == "WHITE":
            depth_first_minmax(child)
            if value_min >= child.min:
                value_min = child.min
                parent.minchild = child
            if value_max < child.max:
                value_max = child.max
                parent.maxchild = child
    parent.color = "BLACK"
    if len(parent.adjacents) == 0:
        parent.min = parent.value
        parent.max = parent.value
    else:
        parent.min = value_min
        parent.max = value_max
