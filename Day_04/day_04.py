#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 10:16:46 2021

@author: shavak
"""

import numpy as np

n = 5

f = open("input.txt", "r")
calls = [int(x) for x in f.readline().split(",")]
line = f.readline()
M = {}
S = []
q = 0
while line != "":
    r = 0
    w = 0
    for i in range(n):
        c = 0
        for u in f.readline().split():
            v = int(u)
            w += v
            if v not in M.keys():
                M[v] = []
            M[v].append((q, r, c))
            c += 1
        r += 1
    S.append(w)
    q += 1
    line = f.readline()
f.close()

X = [np.zeros((n, n), dtype = bool) for _ in range(q)]
Y = [False for _ in range(q)]

for k in calls:
    bingos = []
    if k not in M.keys():
        continue
    for (j, r, c) in M[k]:
        B = X[j]
        if not B[r, c]:
            B[r, c] = True
            S[j] -= k
            if ((np.sum(B[r, :]) == n) or (np.sum(B[:, c]) == n)) and not Y[j]:
                bingos.append(j)
                Y[j] = True
    for z in bingos:
        print("Bingo! Board Number: {}. Score: {}.".format(z, S[z] * k))
            