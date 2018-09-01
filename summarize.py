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


def plot_moments(data_file, move, zoom=0, oname=None, moments=None):
    """Plot the mean and stdev payoffs and save as TikZ file."""
    save = False
    if oname is None:
        oname = data_file
    else:
        save = True
    if moments is None:
        moments = get_moments(data_file, move)
    plt.style.use('seaborn-whitegrid')
    plt.grid('True')
    lines = {'linestyle': 'None'}
    plt.rc('lines', **lines)
    max_moves = np.arange(zoom, np.shape(moments)[0]) + 1
    paul_plot, = plt.plot(max_moves, moments[zoom:, 0], 'o', color='#3C9BF5')
    carole_plot, = plt.plot(max_moves, moments[zoom:, 2], 'o', color='#B5075F')
    plt.errorbar(
        max_moves,
        moments[zoom:, 0],
        capsize=3,
        yerr=moments[zoom:, 1],
        color='#3C9BF5')
    plt.errorbar(
        max_moves,
        moments[zoom:, 2],
        capsize=3,
        yerr=moments[zoom:, 3],
        color='#B5075F')
    plt.legend(
        [paul_plot, carole_plot], ["Paul " + move, "Carole " + move],
        loc='best')
    plt.xlabel('Number of Moves in Game')
    plt.ylabel('Average Payoff')
    plt.xticks(max_moves)
    plt.title(oname)
    if save:
        tikz_save(oname + '.tex')
    plt.show()


def histogram_data(data_file, move, num_move, bins=None, oname=None):
    """Plot the payoff distribution at a particular move count."""
    save = False
    if oname is None:
        oname = data_file
    else:
        save = True
    paul_data, carole_data = get_moments(data_file, move, num_move)
    plt.style.use('seaborn-whitegrid')
    plt.grid('True')
    lines = {'linestyle': 'None'}
    plt.rc('lines', **lines)
    if bins is None:
        plt.hist(
            [paul_data, carole_data],
            color=['#3C9BF5', '#B5075F'],
            stacked=True)
    else:
        plt.hist(
            [paul_data, carole_data],
            bins,
            color=['#3C9BF5', '#B5075F'],
            stacked=True)
    plt.legend(
        {
            'Paul ' + move: '#3C9BF5',
            'Carole ' + move: '#B5075F'
        }, loc='best')
    plt.xlabel('Payoff')
    plt.ylabel('Occurrences')
    plt.title(oname)
    if save:
        tikz_save(oname + '.tex')
    plt.show()


def get_moments(data_file, move, num_move=None):
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
    graphs_per_move = data[-1][1] + 1
    if num_move is not None:
        i = num_move - 1
        start = graphs_per_move * i
        subset_paul = paul_data[4][:][start:start + graphs_per_move]
        subset_carole = carole_data[4][:][start:start + graphs_per_move]
        return subset_paul, subset_carole
    max_moves = data[-1][0]
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
