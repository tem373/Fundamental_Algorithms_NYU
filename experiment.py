#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Play the Game a bunch of times and save results.

@author: Alex Crain
"""
import sys
from algorithm import dfs_nash
from graph import Graph


def main():
    """Run experiments from the command line"""
    if len(sys.argv) != 5 or len(sys.argv) != 6:
        print("Usage: experiment.py trials_per_moves max_moves", end="")
        print("game_type output_file distribution")
        return -1
    trials_per_moves = sys.argv[1]
    max_moves = sys.argv[2]
    game_type = sys.argv[3]
    output_file = sys.argv[4]
    spread = sys.argv[5]
    if game_type < 3:
        trials = experiment(trials_per_moves, max_moves, spread, game_type)
    else:
        print("Unknown game type", game_type)
    save_trials(trials, output_file)
    return 0


def save_trials(trials, output_file):
    


def experiment(trials_per_moves, max_moves, distribution, rand_graph):
    """Play standard Game up to a given numer of possible moves."""
    trials = list()
    for i in range(1, max_moves + 1):
        for j in range(trials_per_moves):
            graph_instance = Graph(i, distribution, rand_graph)
            root = graph_instance.vertices[0]
            dfs_nash(root)
            trials.append(Trial(j, i, "PAUL", root.maximin).as_list())
            trials.append(Trial(j, i, "CAROLE", root.minimax).as_list())
    return trials


def rand_graph_experiment(trials_per_moves, max_moves, distribution):
    """Play random graph Game up to a given numer of possible moves."""
    trials = list()
    for i in range(1, max_moves + 1):
        for j in range(trials_per_moves):
            graph_instance = Graph(i, distribution, rand_graph=1)
            root = graph_instance.vertices[0]
            dfs_nash(root)
            trials.append(Trial(j, i, "PAUL", root.maximin).as_list())
            trials.append(Trial(j, i, "CAROLE", root.minimax).as_list())
    return trials


class Trial:
    """Holds parameters and results of one run of the game."""

    def __init__(self, num_id, num_moves, first_player, payoff):
        self.num_id = num_id
        self.num_moves = num_moves
        self.first_player = first_player
        self.set_last_player(first_player, num_moves)
        self.payoff = payoff

    def set_last_player(self, first_player, num_moves):
        """Figure out who moved last."""
        if first_player != "PAUL" and first_player != "CAROLE":
            raise ValueError('Unknown player ' + first_player + ' got a move.')
        if num_moves % 2:
            self.last_player = first_player
        else:
            if first_player == "PAUL":
                self.last_player = "CAROLE"
            else:
                self.last_player = "PAUL"

    def as_list(self):
        """Get a list of all the trial data."""
        return [
            self.num_id, self.num_moves, self.first_player, self.last_player,
            self.payoff
        ]


if __name__ == '__main__':
    main()
