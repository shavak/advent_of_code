#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:50:40 2022

@author: shavak
"""

input_file = "input.txt"

X_min = -50
X_max = 50
Y_min = -50
Y_max = 50
Z_min = -50
Z_max = 50

R = {}

with open(input_file, "r") as f:
    for line in f.readlines():
        flip, coords = line.split()
        Q = [[int(c) for c in u[2 : ].split("..")] for u in coords.split(",")]
        x1 = max(Q[0][0], X_min)
        x2 = min(Q[0][1], X_max)
        y1 = max(Q[1][0], Y_min)
        y2 = min(Q[1][1], Y_max)
        z1 = max(Q[2][0], Z_min)
        z2 = min(Q[2][1], Z_max)
        if flip == "on":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                            R[(x, y, z)] = 1
        if flip == "off":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        if (x, y, z) in R:
                            R.pop((x, y, z))
    
print("\nAnswer = {}.".format(len(R.keys())))