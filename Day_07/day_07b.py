#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:30:20 2021

@author: shavak
"""

# What I've done for this one feels inefficient. I'll think about a better way
# to deal with the non-linear fuel cost.

import numpy as np

H = {}
l = np.infty
r = -np.infty

f = open("input.txt", "r")
for k in [int(s) for s in f.readline().split(",")]:
    if k not in H.keys():
        H[k] = 1
    else:
        H[k] += 1
    if k < l:
        l = k
    if k > r:
        r = k
f.close()


y = np.infty

for j in range(l + 1, r + 1, 1):
    v = 0
    for k in H.keys():
        # Recalculate everything. Ugh.
        d = abs(k - j)
        v += (d * (d + 1) * H[k]) // 2
    if v < y:
        y = v
        
print("Answer = {}".format(y))