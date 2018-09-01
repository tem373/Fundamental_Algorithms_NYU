#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Play the Game a bunch of times and save results.

@author: Alex Crain
"""
from sys import argv
from astropy.table import Table
from algorithm import dfs_nash
from graph import Graph


def main():
    """Run experiments from the command line."""
    if len(argv) != 6:
        print("Usage: experiment.py trials_per_moves max_moves", end=" ")
        print("game_type output_file spread")
        return -1
    trials_per_moves = int(argv[1])
    max_moves = int(argv[2])
    game_type = int(argv[3])
    output_file = argv[4]
    if output_file[-5:] != '.hdf5':
        output_file += '.hdf5'
    spread = argv[5]
    if game_type < 3:
        trials = experiment(trials_per_moves, max_moves, spread, game_type)
    else:
        print("Unknown game type", game_type)
    save_trials(trials, output_file)
    return 0


def save_trials(trials, output_file):
    """Save experimental data."""
    trial_table = Table(
        rows=trials,
        names=('Number of Moves', 'Graph ID', 'First Mover Paul',
               'Last Mover Paul', 'Payoff'),
        meta={'name': output_file})
    trial_table.write(output_file, path='trials')
    return 0


def read_trials(input_file):
    """Read experimental data."""
    return Table.read(input_file, path='trials')


def experiment(trials_per_moves, max_moves, distribution, game_type):
    """Play standard Game up to a given numer of possible moves."""
    trials = list()
    for i in range(1, max_moves + 1):
        for j in range(trials_per_moves):
            graph_instance = Graph(i, distribution, game_type)
            root = graph_instance.vertices[0]
            dfs_nash(root)
            trials.append(Trial(j, i, "PAUL", root.maximin).as_list())
            trials.append(Trial(j, i, "CAROLE", root.minimax).as_list())
    return trials


def player_to_bool(player):
    """Return true for Paul, false for Carole."""
    if player != "PAUL" and player != "CAROLE":
        raise ValueError('Unknown player ' + player + ' got a move.')
    if player == "PAUL":
        player = True
    elif player == "CAROLE":
        player = False
    else:
        raise ValueError('Unknown player ' + player + ' got a move.')
    return player


class Trial:
    """Holds parameters and results of one run of the game."""

    def __init__(self, num_id, num_moves, first_player, payoff):
        self.num_id = num_id
        self.num_moves = num_moves
        self.first_player = player_to_bool(first_player)
        self.set_last_player(first_player, num_moves)
        self.payoff = payoff

    def set_last_player(self, first_player, num_moves):
        """Figure out who moved last."""
        if num_moves % 2:
            self.last_player = player_to_bool(first_player)
        else:
            if first_player == "PAUL":
                self.last_player = player_to_bool("CAROLE")
            else:
                self.last_player = player_to_bool("PAUL")

    def as_list(self):
        """Get a list of all the trial data."""
        return [
            self.num_moves, self.num_id, self.first_player, self.last_player,
            self.payoff
        ]


if __name__ == '__main__':
    main()
