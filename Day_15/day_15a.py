#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:53:50 2022

@author: shavak
"""

import numpy as np

E = {}
n = 0
top = []
mid = []
bot = []
with open("input.txt", "r") as f:
    mid = [int(x) for x in f.readline().strip()]
    bot = [int(x) for x in f.readline().strip()]
    c = len(mid)
    while c > 0:
        for j in range(c):
            E[n] = []
            if j > 0:
                E[n].append((n - 1, mid[j - 1]))
            if len(top) > 0:
                E[n].append((n - c, top[j]))
            if j + 1 < c:
                E[n].append((n + 1, mid[j + 1]))
            if len(bot) > 0:
                E[n].append((n + c, bot[j]))
            n += 1
        top = mid
        mid = bot
        bot = [int(x) for x in f.readline().strip()]
        c = len(mid)

d = np.ones(n, dtype = int) * np.inf
d[0] = 0
Q = list(range(n))
l = n

while l > 0:
    k = 0
    for i in range(l):
        if d[Q[i]] < d[Q[k]]:
            k = i
    v = Q[k]
    Q[k] = Q[l - 1]
    Q.pop()
    l -= 1
    for (u, w) in E[v]:
        d[u] = min(d[u], d[v] + w)

print("Answer = {}.".format(d[n - 1]))