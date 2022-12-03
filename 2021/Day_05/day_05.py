#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:10:58 2021

@author: shavak
"""

diagonals = True

coordinate_parse = lambda w: tuple(int(p) for coord in
                                   [s.split(",") for s in w.split("->")]
                                   for p in coord)

M = {}
c = 0
with open("input.txt", "r") as f:
    for line in f:
        x1, y1, x2, y2 = coordinate_parse(line)
        dx = x2 - x1
        dy = y2 - y1
        if (dx == 0):
            if (dy < 0):
                (y1, y2) = (y2, y1)
            for y in range(y1, y2 + 1):
                p = (x1, y)
                if p not in M.keys():
                    M[p] = 1
                else:
                    M[p] += 1
                    c += (M[p] == 2)
        elif (dy == 0):
            if (dx < 0):
                (x1, x2) = (x2, x1)
            for x in range(x1, x2 + 1):
                p = (x, y1)
                if p not in M.keys():
                    M[p] = 1
                else:
                    M[p] += 1
                    c += (M[p] == 2)
        elif ((dx == dy) or (dx == -dy)) and diagonals:
            u = v = 1
            q = dx
            if dx < 0:
                u = -1
                q = -dx
            if dy < 0:
                v = -1
            for i in range(q + 1):
                p = (x1 + u * i, y1 + v * i)
                if p not in M.keys():
                    M[p] = 1
                else:
                    M[p] += 1
                    c += (M[p] == 2)
        else:
            continue

print("Answer = {}".format(c))
            
            