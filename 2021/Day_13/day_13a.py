#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:23:52 2022

@author: shavak
"""

import numpy as np

def reflect(r, c, axis, k):
    t = 2 * k
    if r > k and r <= t and axis == 0:
        return (t - r, c)
    elif c > k and c <= t and axis == 1:
        return (r, t - c)
    else:
        return (r, c)

pts = []
m = 0
n = 0

f = open("input.txt", "r")

line = f.readline()
while line != "\n":
    (c, r) = tuple(int(s) for s in line.strip().split(","))
    if m < r:
        m = r
    if n < c:
        n = c
    pts.append((r, c))
    line = f.readline()

X = np.zeros((m + 1, n + 1), dtype = bool)
for p in pts:
    X[p] = True

fold = f.readline().split()[2].split("=")
axis = 0 if fold[0] == "y" else  1
k = int(fold[1])
for (r, c) in pts:
    (u, v) = reflect(r, c, axis, k)
    X[u, v] = True
    if (u, v) != (r, c):
        X[r, c] = False
f.close()

print("Answer = {}".format(np.sum(X)))