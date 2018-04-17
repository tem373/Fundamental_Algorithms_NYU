# -*- coding: utf-8 -*-
"""
Demonstrates a working implementation of the game.

Created on Mon Apr 16 02:52:11 2018

@author: Alex Crain
"""
import numpy as np
from algorithm import game
from graph import Graph

payoff_paul_goes_first = list()
payoff_carole_goes_first = list()
for i in range(1000):
    g = Graph(8)
    payoff_paul_goes_first.append(game(g.vertices[0], "PAUL"))
    payoff_carole_goes_first.append(game(g.vertices[0], "CAROLE"))

print("Paul first, even number of moves:", np.mean(payoff_paul_goes_first))
print("Carole first, even number of moves:", np.mean(payoff_carole_goes_first))

payoff_paul_goes_first = list()
payoff_carole_goes_first = list()
for i in range(1000):
    g = Graph(9)
    payoff_paul_goes_first.append(game(g.vertices[0], "PAUL"))
    payoff_carole_goes_first.append(game(g.vertices[0], "CAROLE"))

print("Paul first, odd number of moves:", np.mean(payoff_paul_goes_first))
print("Carole first, odd number of moves:", np.mean(payoff_carole_goes_first))
