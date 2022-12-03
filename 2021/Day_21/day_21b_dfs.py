#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 02:04:53 2022

@author: shavak
"""

input_file = "input.txt"

W = 21
k = 10

def dirac_dice_roll_3():
    D = {}
    for e in range(1, 4):
        for f in range(1, 4):
            for g in range(1, 4):
                r = e + f + g
                if r not in D:
                    D[r] = 1
                else:
                    D[r] += 1
    return D

def player_turn(s, i, x):
    g = (i + x) % k
    h = (k if g == 0 else g)
    return s + h, h
    
def dirac_universe_search(i, j):
    a = 0
    b = 0
    D = dirac_dice_roll_3()
    stack = [(0, 0, i, j, True, 1)]
    while stack:
        s, t, i, j, player_1, m = stack.pop()
        if player_1:
            for x in D:
                u, h = player_turn(s, i, x)
                z = m * D[x]
                if u >= W:
                    a += z
                else:
                    stack.append((u, t, h, j, False, z))
        else:
            for x in D:
                u, h = player_turn(t, j, x)
                z = m * D[x]
                if u >= W:
                    b += z
                else:
                    stack.append((s, u, i, h, True, z))
    return a, b

with open(input_file, "r") as f:
    i = int(f.readline().split(": ")[1])
    j = int(f.readline().split(": ")[1])

a, b = dirac_universe_search(i, j)
print("\nAnswer = {}.".format(max(a, b)))