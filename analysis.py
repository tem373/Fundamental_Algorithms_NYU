"""
Run some trials of the game and save relevant parameters
for analysis.


@author: Alex Crain
"""

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
