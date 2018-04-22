#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compute and display summary statistics.

@author: Alex Crain
"""
import numpy as np
from statistics import mean, stdev
from experiment import read_trials

def get_moments(data_file):
    data = read_trials(data_file)
    paul_first_data = data[np.where(data[2][:] == True)]
    carole_first_data = data[np.where(data[2][:] == False)]
    max_moves = data[-1][0]
    graphs_per_move = data[-1][1] + 1
    moments_paul_carole = np.zeros([max_moves, 4])
    for i in range(max_moves):
        start = graphs_per_move * i
        subset_paul = paul_first_data[4][:][start:start + graphs_per_move]
        subset_carole = carole_first_data[4][:][start:start + graphs_per_move]
        moments_paul_carole[i][0] = mean(subset_paul)
        moments_paul_carole[i][1] = stdev(subset_paul)
        moments_paul_carole[i][2] = mean(subset_carole)
        moments_paul_carole[i][3] = stdev(subset_carole)
    return moments_paul_carole

def plot_moments(data_file, moments=None):
    if moments is None:
        moments = get_moments(data_file)
    