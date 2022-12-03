#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 07:52:46 2021

@author: shavak
"""

import numpy as np

H = {}
l = np.infty
r = -np.infty
x = 0
y = 0
n = 0

f = open("input.txt", "r")
for k in [int(s) for s in f.readline().split(",")]:
    if k not in H.keys():
        H[k] = 1
    else:
        H[k] += 1
    y += k
    if k < l:
        l = k
    if k > r:
        r = k
    n += 1
f.close()

x = l
y -= n * l
q = H[l]
v = y

for j in range(l + 1, r + 1, 1):
    v += 2 * q - n
    if v < y:
        y = v
        x = j
    if j in H.keys():
        q += H[j]
    
print("Answer = {}".format(y))        