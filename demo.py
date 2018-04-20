# -*- coding: utf-8 -*-
"""
Demonstrates a working implementation of the Game.

@author: Alex Crain
"""
import numpy as np
from algorithm import game, dfs_nash
from graph import Graph

payoff_paul_goes_first = list()
payoff_carole_goes_first = list()
for i in range(1,8):
    payoff_paul_goes_first = list()
    payoff_carole_goes_first = list()
    for j in range(10):
        g = Graph(i, rand_graph=1)
        dfs_nash(g.vertices[0])
        payoff_paul_goes_first.append(g.vertices[0].maximin)
        payoff_carole_goes_first.append(g.vertices[0].minimax)
    print("Move count", i)
    print("Paul first:", np.mean(payoff_paul_goes_first), np.var(payoff_paul_goes_first))
    print("Carole first:", np.mean(payoff_carole_goes_first), np.var(payoff_carole_goes_first))

#g = Graph(6)
#paypaul = game(g.vertices[0], "PAUL")
#paycaro = game(g.vertices[0], "CAROLE")
#paulfirst = g.vertices[0].maximin
#carofirst = g.vertices[0].minimax
#
## Should give Paul 6 and Carole 3.
#g = Graph(3)
#g.vertices[7].value = 5
#g.vertices[8].value = 3
#g.vertices[9].value = 1
#g.vertices[10].value = 8
#g.vertices[11].value = 2
#g.vertices[12].value = 7
#g.vertices[13].value = 6
#g.vertices[14].value = 4
#pf = game(g.vertices[0], "PAUL")
#cf = game(g.vertices[0], "CAROLE")
#print(pf)
#print(cf)
#print(g.vertices[0].maximin)
#print(g.vertices[0].minimax)
