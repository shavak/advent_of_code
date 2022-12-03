#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:10:13 2022

@author: shavak
"""

input_file = "input_b.txt"

Y = ["A", "B", "C", "D"]
Z = [3, 5, 7, 9]
R = {T : i for (T, i) in zip(Y, Z)}
E = {T : h for (T, h) in zip(Y, [10**q for q in range(4)])}
L = 23

F = None
G = None

def state_diagram_correspondence():
    Q = list(zip(range(11), [1, 2] + [i + 1 for i in Z] + [11]))
    f = {x : (1, j) for (x, j) in Q}
    g = {(1, j) : x for (x, j) in Q}
    x = 7
    for i in range(2, 6):
        for j in Z:
            f[x] = (i, j)
            g[(i, j)] = x
            x += 1
    return f, g

def encode_diagram(diagram = None):
    if diagram == None:
        return tuple(["."] * 7 + ["A", "B", "C", "D"] * 4)
    res_lst = [0] * L
    for h in range(L):
        (i, j) = F[h]
        res_lst[h] = diagram[i][j]
    return tuple(res_lst)

def amphipod_moves(state, p):
    i, j = F[p]
    T = state[p]
    l = R[T]
    if i == 1:
        # Amphipod is in the hallway - the only place that it can go is to its
        # designated room.
        k = 5
        while k > 1:
            U = state[G[(k, l)]]
            if U == ".":
                break
            elif U != T:
                return []
            k -= 1
        if k == 1:
            return []
        # The destination is (k, l).
        s = -1 if j > l else 1
        x = j
        while x != l:
            x += s
            if (i, x) in G and state[G[(i, x)]] != ".":
                return []
        q = G[(k, l)]
        temp_state = list(state)
        (temp_state[p], temp_state[q]) = (temp_state[q], temp_state[p])
        return [(tuple(temp_state), ((k - 1) + s * (l - j)) * E[T])]
    # The amphipod is in a room. Let's see if it can move.
    if j == l:
        # This amphipod is already in its room.
        k = 5
        while k >= i:
            U = state[G[(k, j)]]
            if U != T:
                break
            k -= 1
        if k == i:
            # Every amphipod below it is of the same type - no need to move!
            return []
    if i > 2 and state[G[(i - 1, j)]] != ".":
        # There is another amphipod above this amphipod.
        return []
    res = []
    x = j - 1
    room_switch = False
    while x >= 1:
        if x in Z:
            room_switch = room_switch or (x == l)
        else:
            q = G[(1, x)]
            if state[q] != ".":
                break
            temp_state = list(state)
            (temp_state[p], temp_state[q]) = (temp_state[q], temp_state[p])
            res.append((tuple(temp_state), (i - 1 + j - x) * E[T]))
        x -= 1
    x = j + 1
    while x <= 11:
        if x in Z:
            room_switch = room_switch or (x == l)
        else:
            q = G[(1, x)]
            if state[q] != ".":
                break
            temp_state = list(state)
            (temp_state[p], temp_state[q]) = (temp_state[q], temp_state[p])
            res.append((tuple(temp_state), (i - 1 + x - j) * E[T]))
        x += 1
    if room_switch:
        k = 5
        while k > 1:
            U = state[G[(k, l)]]
            if U == ".":
                break
            elif U != T:
                return res
            k -= 1
        if k == 1:
            return res
        q = G[(k, l)]
        temp_state = list(state)
        (temp_state[p], temp_state[q]) = (temp_state[q], temp_state[p])
        res.append((tuple(temp_state),
                    ((i - 1) + abs(j - l) + (k - 1)) * E[T]))
    return res

def all_edges(state):
    res = []
    for p in range(23):
        if state[p] != ".":
            res.extend(amphipod_moves(state, p))
    return res

def build_graph(starting_state):
    E = {}
    stack = [starting_state]
    while stack:
        state = stack.pop()
        adj = all_edges(state)
        E[state] = adj
        for (node, _) in adj:
            if node not in E:
                stack.append(node)
    return list(E.keys()), E

def dijkstra(source, V, E):
    d = {v : float("inf") for v in V}
    d[source] = 0
    Q = [0]
    Q.append(source)
    idx_map = {}
    idx_map[source] = 1
    n = 1
    for v in V:
        if v == source:
            continue
        Q.append(v)
        n += 1
        idx_map[v] = n
    Q[0] = n
    def sift_up(i):
        while i > 1:
            j = i // 2
            if d[Q[i]] < d[Q[j]]:
                (idx_map[Q[i]], idx_map[Q[j]]) = (idx_map[Q[j]], idx_map[Q[i]])
                (Q[j], Q[i]) = (Q[i], Q[j])
                i = j
            else:
                break
        return
    def sift_down(i):
        j = 2 * i
        while j <= Q[0]:
            if j + 1 < Q[0] and d[Q[j + 1]] < d[Q[j]]:
                j += 1
            if d[Q[i]] > d[Q[j]]:
                (idx_map[Q[i]], idx_map[Q[j]]) = (idx_map[Q[j]], idx_map[Q[i]])
                (Q[i], Q[j]) = (Q[j], Q[i])
                i = j
                j = 2 * i
            else:
                break
    while Q[0] > 0:
        u = Q[1]
        Q[1] = Q[Q[0]]
        Q[0] -= 1
        sift_down(1)
        for (v, w) in E[u]:
            s = d[u] + w
            if s < d[v]:
                d[v] = s
                sift_up(idx_map[v])
    return d

starting_diagram = []
with open(input_file, "r") as file_handler:
    for line in file_handler.readlines():
        starting_diagram.append(list(line.rstrip()))
for i in range(3, 5):
    for _ in range(2):
        starting_diagram[i].append(" ")
F, G = state_diagram_correspondence()
starting_state = encode_diagram(starting_diagram)
organised_state = encode_diagram()
V, E = build_graph(starting_state)
d = dijkstra(starting_state, V, E)
print("\nAnswer = {}.".format(d[organised_state]))