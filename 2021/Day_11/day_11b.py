#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:52:08 2022

@author: shavak
"""

import numpy as np

N = 10
E = np.zeros((N, N), dtype = int)
with open("input.txt", "r") as f:
    i = 0
    for line in f:
        j = 0
        for x in line.strip():
            E[i, j] = int(x)
            j += 1
        i += 1

num_flashes = 0
stack = []
F = np.zeros((N, N), dtype = bool)

def perturb_point(u, v):
    global E, num_flashes, stack, F
    if (u < 0) or (u > N - 1) or (v < 0) or (v > N - 1):
        return
    if F[u, v]:
        return
    E[u, v] += 1
    if E[u, v] > 9:
        stack.append((u, v))
        F[u, v] = True
        num_flashes += 1
    return

c = 0
while np.sum(F) < N * N:
    E += 1
    stack = []
    F = np.zeros((N, N), dtype = bool)
    for i in range(N):
        for j in range(N):
            if E[i, j] > 9:
                stack.append((i, j))
                num_flashes += 1
                F[i, j] = True
    while stack:
        p = stack.pop()
        [perturb_point(i, j) for i in range(p[0] - 1, p[0] + 2)\
         for j in range(p[1] - 1, p[1] + 2)]
    E[F] = 0
    c += 1

print("Answer = {}".format(c))