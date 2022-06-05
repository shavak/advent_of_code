#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:10:13 2022

@author: shavak
"""

input_file = "test_input_b.txt"

Y = ["A", "B", "C", "D"]
Z = [3, 5, 7, 9]
G = {T : i for (T, i) in zip(Y, Z)}
E = {T : h for (T, h) in zip(Y, [10**q for q in range(4)])}
L = 23

def state_diagram_correspondence():
    Q = list(zip(range(11), [1, 2] + [i + 1 for i in Z] + [11]))
    f = {h : (1, j) for (h, j) in Q}
    g = {(1, j) : h for (h, j) in Q}
    h = 7
    for i in range(2, 6):
        for j in Z:
            f[h] = (i, j)
            g[(i, j)] = h
            h += 1
    return f, g

def encoded_state(state_map, diagram = None):
    if diagram == None:
        return tuple(["."] * 7 + ["A", "B", "C", "D"] * 4)
    res_lst = [0] * L
    for h in range(L):
        (i, j) = state_map[h]
        res_lst[h] = diagram[i][j]
    return tuple(res_lst)

def adjacent_states(S):
    pass

def build_graph(starting_state):
    pass

def dijkstra(source, V, E):
    pass

starting_diagram = []
with open(input_file, "r") as file_handler:
    for line in file_handler.readlines():
        starting_diagram.append(list(line.rstrip()))
for i in range(3, 5):
    for _ in range(2):
        starting_diagram[i].append(" ")
state_map, diagram_map = state_diagram_correspondence()
starting_state = encoded_state(state_map, starting_diagram)
organised_state = encoded_state(state_map)
V, E = build_graph(starting_state)
d = dijkstra(starting_state, V, E)
print("\nAnswer = {}.".format(d[organised_state]))