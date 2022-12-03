#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 08:17:38 2022

@author: shavak
"""

import numpy as np

E = {}
V = {}

def add_edge(u, v):
    global E
    if u not in E.keys():
        E[u] = []
    E[u].append(v)

def add_visitation_policy(u):
    global V
    if u not in V.keys():
        V[u] = 2 if u == u.lower() else np.inf
     
with open("input.txt", "r") as f:
    for line in f:
        x = [s.strip() for s in line.split("-")]
        add_edge(x[0], x[1])        
        add_edge(x[1], x[0])
        add_visitation_policy(x[0])
        add_visitation_policy(x[1])

V["end"] = 1
path = ["start"]
ptr = [0]
V["start"] = 0
num_paths = 0
double_dragon = False

while path:
    x = path[-1]
    if x == "end":
        num_paths += 1
        V[path.pop()] += 1
        ptr.pop()
    else:
        n = len(E[x])
        y = ""
        while ptr[-1] < n:
            y = E[x][ptr[-1]]
            if V[y] > (0 if (not double_dragon or y == "end") else 1):
                break
            ptr[-1] += 1
        if ptr[-1] == n:
            y = path.pop()
            V[y] += 1
            if (y != "start" and y != "end" and V[y] == 1):
                double_dragon = False
            ptr.pop()
        else:
            path.append(y)
            V[y] -= 1
            double_dragon = double_dragon or (V[y] == 0 and y != "end")
            ptr[-1] += 1
            ptr.append(0)

print("Answer = {}".format(num_paths))