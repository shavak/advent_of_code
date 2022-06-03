#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:10:13 2022

@author: shavak
"""

input_file = "test_input.txt"

G = {"A" : 3, "B" : 5, "C" : 7, "D" : 9}

E = {T : h for (T, h) in zip(G.keys(), [10**q for q in range(4)])}

def diagram_copy(diagram):
    res = []
    n = len(diagram)
    for i in range(n):
        res.append(diagram[i].copy())
    return res

def starting_locator(diagram):
    res = {}
    for i in range(2, 4):
        for j in range(3, 10, 2):
            if (diagram[i][j], 1) not in res:
                res[(diagram[i][j], 1)] = (i, j)
            else:
                res[(diagram[i][j], 2)] = (i, j)
    return res

def is_organised(diagram, T):
    return diagram[2][G[T]] == T and diagram[3][G[T]] == T

def is_fully_organised(diagram):
    ans = True
    for T in G.keys():
        ans = ans and is_organised(diagram, T)
    return ans

def energy_usage(T, i, j, k, l):
    return abs((k - i) * (l - j)) * E[T]

def amphipod_moves(diagram, locator, type_key):
    i, j = locator[type_key]
    T = type_key[0]
    if i == 3 and (j == G[T] or diagram[2][j] != "."):
        # Amphipod is either already where it needs to be or cannot move just
        # yet.
        return []
    if i == 1:
        # Amphipod is in the hallway - the only place that it can go is to its
        # designated room.
        l = G[T]
        k = -1
        if diagram[2][l] == "." and diagram[3][l] == T:
            k = 2
        elif diagram[2][l] == "." and diagram[3][l] == ".":
            k = 3
        else:
            return []
        # The destination is (k, l).
        q = j
        s = -1 if q > l else 1
        while q != l:
            q += s
            if diagram[i][q] != ".":
                return []
        D = diagram_copy(diagram)
        D[i][j] = "."
        D[k][l] = T
        H = locator.copy()
        H[type_key] = (k, l)
        return [(D, H, energy_usage(T, i, j, k, l))]
    else:
        # Amphipod is in a room.
        # Investigate the possible "hallway" moves and then check whether
        # room-to-room is possible.
        # First go left into the hallway.
        res = []
        q = j - 1
        l = G[T]
        r2r = False
        while diagram[1][q] == ".":
            D = diagram_copy(diagram)
            D[i][j] = "."
            D[1][q] = T
            H = locator.copy()
            H[type_key] = (1, q)
            res.append((D, H, energy_usage(T, i, j, 1, q)))
            r2r = q == l
            q -= 1
        q = j + 1
        while diagram[1][q] == ".":
            D = diagram_copy(diagram)
            D[i][j] = "."
            D[1][q] = T
            H = locator.copy()
            H[type_key] = (1, q)
            res.append((D, H, energy_usage(T, i, j, 1, q)))
            r2r = q == l
            q += 1
        if r2r and diagram[2][l] == ".":
            # Room-to-room?
            k = -1
            if diagram[3][l] == T:
                k = 2
            elif diagram[3][l] == ".":
                k = 3
            else:
                return res
            D = diagram_copy(diagram)
            D[i][j] = "."
            D[k][l] = T
            H = locator.copy()
            H[type_key] = (k, l)
            res.append((D, H, energy_usage(T, i, j, 1, l)\
                        + energy_usage(T, 1, l, k, l)))
        return res
    return []    

def minimum_organising_energy(diagram):
    minimum_energy = float("inf")
    stack = [(diagram, starting_locator(diagram), 0)]
    while stack:
        diagram, locator, energy_used = stack.pop()
        if is_fully_organised(diagram):
            minimum_energy = min(minimum_energy, energy_used)
            continue
        for T in G.keys():
            if not is_organised(diagram, T):
                # If the amphipod of Type T is not already organised, then it
                # can be moved.
                for (D, L, h) in amphipod_moves(diagram, locator, (T, 1)):
                    v = energy_used + h
                    if v < minimum_energy:
                        stack.append((D, L, v))
                for (D, L, h) in amphipod_moves(diagram, locator, (T, 2)):
                    v = energy_used + h
                    if v < minimum_energy:
                        stack.append((D, L, v))
    return minimum_energy

starting_diagram = []
with open(input_file, "r") as f:
    for line in f.readlines():
        starting_diagram.append(list(line.rstrip()))
for i in range(3, 5):
    for _ in range(2):
        starting_diagram[i].append(" ")

print("\nAnswer = {}.".format(minimum_organising_energy(starting_diagram)))