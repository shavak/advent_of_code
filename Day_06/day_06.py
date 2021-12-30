#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:30:28 2021

@author: shavak
"""

states = [0, 1, 2, 3, 4, 5, 6, 7, 8]
days = 256
S = {k : 0 for k in states}
f = open("input.txt", "r")
for k in [int(x) for x in f.readline().split(",")]:
    S[k] += 1
f.close()

for i in range(days):
    y = S[6]
    for j in range(5, -1, -1):
        x = S[j]
        S[j] = y
        y = x
    S[6] = y + S[7]
    S[7] = S[8]
    S[8] = y

print("Answer = {}".format(sum(S.values())))
        