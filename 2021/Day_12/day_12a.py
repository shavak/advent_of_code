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
        V[u] = 1 if u == u.lower() else np.inf

with open("input.txt", "r") as f:
    for line in f:
        x = [s.strip() for s in line.split("-")]
        add_edge(x[0], x[1])        
        add_edge(x[1], x[0])
        add_visitation_policy(x[0])
        add_visitation_policy(x[1])

path = ["start"]
ptr = [0]
V["start"] -= 1
num_paths = 0

while path:
    node = path[-1]
    if node == "end":
        num_paths += 1
        V[path.pop()] += 1
        ptr.pop()
    else:
        n = len(E[node])
        while ptr[-1] < n:
            if V[E[node][ptr[-1]]] > 0:
                break
            ptr[-1] += 1
        if ptr[-1] == n:
            V[path.pop()] += 1
            ptr.pop()
        else:
            path.append(E[node][ptr[-1]])
            ptr[-1] += 1
            V[path[-1]] -= 1
            ptr.append(0)

print("Answer = {}".format(num_paths))