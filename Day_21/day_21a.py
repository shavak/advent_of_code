#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 00:15:47 2022

@author: shavak
"""

input_file = "input.txt"

W = 1000
g = 100
p = 10

def simulate_game_deterministic(x, y):
    player_1 = True
    a = 0
    b = 0
    d = 0
    while a < W and b < W:
        h = 0
        for _ in range(3):
            d += 1
            r = d % g
            h += g if r == 0 else r
        if player_1:
            q = (x + h) % p
            x = p if q == 0 else q
            a += x
            player_1 = False
        else:
            q = (y + h) % p
            y = p if q == 0 else q
            b += y
            player_1 = True
    return d, a, b

with open(input_file, "r") as f:
    x = int(f.readline().split(": ")[1])
    y = int(f.readline().split(": ")[1])

d, a, b = simulate_game_deterministic(x, y)
print("\nAnswer = {}.".format(d * min(a, b)))