#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compute and display summary statistics.

@author: Alex Crain
"""
from statistics import mean, stdev
import numpy as np
import matplotlib.pyplot as plt
from matplotlib2tikz import save as tikz_save
from experiment import read_trials


def plot_moments(data_file, move, oname=None, moments=None):
    """Plot the mean and stdev for the first movers and save as TikZ file."""
    save = False
    if oname is None:
        oname = data_file
    else:
        save = True
    if moments is None:
        moments = get_moments(data_file, move)
    plt.style.use('dark_background')
    plt.grid('True')
    max_moves = np.arange(np.shape(moments)[0]) + 1
    paul_plot, = plt.plot(max_moves, moments[:, 0], 'o', color='#3C9BF5')
    carole_plot, = plt.plot(max_moves, moments[:, 2], 'o', color='#B5075F')
    plt.legend(
        [paul_plot, carole_plot], ["Paul " + move, "Carole " + move],
        loc='center right')
    plt.xlabel('Number of Moves in Game')
    plt.ylabel('Payoff')
    plt.xticks(max_moves)
    plt.title(oname)
    if save:
        tikz_save(oname + '.tex')
    plt.show()


def get_moments(data_file, move='First'):
    """Get mean and stdev for payoffs under first or last mover conditions."""
    data = read_trials(data_file)
    if move == 'First':
        paul_data = data[np.where(data[2][:])]
        carole_data = data[np.where(~data[2][:])]
    elif move == 'Last':
        paul_data = data[np.where(data[3][:])]
        carole_data = data[np.where(~data[3][:])]
    else:
        raise ValueError('Move ' + move + ' not recognized.')
    max_moves = data[-1][0]
    graphs_per_move = data[-1][1] + 1
    moments_paul_carole = np.zeros([max_moves, 4])
    for i in range(max_moves):
        start = graphs_per_move * i
        subset_paul = paul_data[4][:][start:start + graphs_per_move]
        subset_carole = carole_data[4][:][start:start + graphs_per_move]
        moments_paul_carole[i][0] = mean(subset_paul)
        moments_paul_carole[i][1] = stdev(subset_paul)
        moments_paul_carole[i][2] = mean(subset_carole)
        moments_paul_carole[i][3] = stdev(subset_carole)
    return moments_paul_carole
