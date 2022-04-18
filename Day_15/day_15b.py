#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:27:42 2022

@author: shavak
"""

import numpy as np

def read_input(input_file):
    A = []
    with open(input_file, "r") as f:
        for row in f.readlines():
            A.append([int(x) for x in row.strip()])
    return A

def apply_tiling(A, m):
    X = np.array(A)
    Y = X.copy()
    wrap = lambda x : x * (x < 9) + 1
    for _ in range(m - 1):
        X = wrap(X)
        Y = np.concatenate((Y, X), axis = 1)
    X = Y.copy()
    for _ in range(m - 1):
        X = wrap(X)
        Y = np.concatenate((Y, X), axis = 0)
    return Y

def build_graph(R):
    r = R.shape[0]
    c = R.shape[1]
    E = {}
    if (r <= 1) and (c <= 1):
        return r * c, E
    n = 0
    mid = None
    for i in range(r):
        top = mid
        mid = R[i]
        bot = None if i == r - 1 else R[i + 1]
        for j in range(c):
            E[n] = []
            if j > 0:
                E[n].append((n - 1, mid[j - 1]))
            if i > 0:
                E[n].append((n - c, top[j]))
            if j + 1 < c:
                E[n].append((n + 1, mid[j + 1]))
            if i + 1 < r:
                E[n].append((n + c, bot[j]))
            n += 1
    return n, E

def dijkstra(n, E):
    d = np.ones(n, dtype = int) * np.inf
    d[0] = 0
    Q = list(range(-1, n))
    Q[0] = n
    B = list(range(1, n + 1))
    def sift_up(i):
        while i > 1:
            j = i // 2
            if d[Q[i]] < d[Q[j]]:
                (B[Q[i]], B[Q[j]]) = (B[Q[j]], B[Q[i]])
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
                (B[Q[i]], B[Q[j]]) = (B[Q[j]], B[Q[i]])
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
                sift_up(B[v])
    return d

A = read_input("input.txt")
R = apply_tiling(A, 5)
n, E = build_graph(R)
d = dijkstra(n, E)

print("Answer = {}.".format(d[n - 1]))
