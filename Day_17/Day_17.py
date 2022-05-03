#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 01:02:16 2022

@author: shavak
"""

import numpy as np

input_file = "input.txt"

def divisors(n):
    ans = []
    d = 1
    while d * d < n:
        if n % d == 0:
            ans.append(d)
            ans.append(n // d)
        d += 1
    if d * d == n:
        ans.append(d)
    return ans

def x_trajectory(u, k):
    if u < 0:
        return -x_trajectory(-u, k)
    if u == 0:
        return 0
    x = 0
    for _ in range(k):
        x += u
        u -= (1 if u != 0 else 0)
    return x

def initial_velocities(x_min, x_max, y_min, y_max):
    res = {}
    max_height = -np.inf
    if (x_min <= 0 <= x_max) and (y_min <= 0 <= y_max):
        res[(0, 0)] = 0
        max_height = 0
    u_min = min(0, x_min)
    u_max = max(0, x_max)
    for y in range(y_min, y_max + 1):
        q = 2 * y
        d = divisors(q if q > 0 else -q)
        for k in d:
            v = (q // k) + k - 1
            if v % 2 == 0:
                v = v // 2
                for u in range(u_min, u_max + 1):
                    x = x_trajectory(u, k)
                    if x_min <= x <= x_max:
                        # Hit!
                        h = 0 if v <= 0 else v * (v + 1) // 2
                        res[(u, v)] = h
                        max_height = max(max_height, h)
    return res, max_height

with open(input_file, "r") as f:
    line = f.readline().split()

tokens = line[2].split("..")
x_min = int(tokens[0][2 : ])
x_max = int(tokens[1][0 : -1])
tokens = line[3].split("..")
y_min = int(tokens[0][2 : ])
y_max = int(tokens[1])

res, max_height = initial_velocities(x_min, x_max, y_min, y_max)

print("Maximum height = {}.".format(max_height))
print("Number of initial velocities = {}.".format(len(res)))
