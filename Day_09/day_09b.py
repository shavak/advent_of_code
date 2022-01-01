#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 11:23:05 2022

@author: shavak
"""

V = []
L = []
used = []
m = 0
n = 0

def biggest_basin():
    b = []
    for p in L:
        a = []
        stack = []
        H = [[False] * n for _ in range(m)]
        i = p[0]
        j = p[1]
        if (not H[i][j]) and (not used[i][j]):    
            stack.append(p)
        while stack:
            q = stack.pop()
            a.append(q)
            if q[1] != 0:
                i = q[0]
                j = q[1] - 1
                if (not H[i][j]) and (not used[i][j]) and (V[i][j] != 9)\
                    and (V[i][j] > V[i][q[1]]):
                    stack.append((i, j))
                    H[i][j] = True
            if q[0] != 0:
                i = q[0] - 1
                j = q[1]
                if (not H[i][j]) and (not used[i][j]) and (V[i][j] != 9)\
                    and (V[i][j] > V[q[0]][j]):
                    stack.append((i, j))
                    H[i][j] = True
            if q[1] != n - 1:
                i = q[0]
                j = q[1] + 1
                if (not H[i][j]) and (not used[i][j]) and (V[i][j] != 9)\
                    and (V[i][j] > V[i][q[1]]):
                    stack.append((i, j))
                    H[i][j] = True
            if q[0] != m - 1:
                i = q[0] + 1
                j = q[1]
                if  (not H[i][j]) and (not used[i][j]) and (V[i][j] != 9)\
                    and (V[i][j] > V[q[0]][j]):
                    stack.append((i, j))
                    H[i][j] = True
        if len(a) > len(b):
            b = a
    return b
        

top_line = ""
mid_line = ""
bot_line = ""

with open("input.txt", "r") as f:
    mid_line = f.readline().strip()
    bot_line = f.readline().strip()
    n = len(mid_line)
    while mid_line != "":
        V.append([])
        for j in range(n):
            x = mid_line[j]
            V[m].append(int(x))
            r = 1 + V[m][j]
            if j != 0:
                r *= x < mid_line[j - 1]
            if top_line != "":
                r *= x < top_line[j]
            if j != n - 1:
                r *= x < mid_line[j + 1]
            if bot_line != "":
                r *= x < bot_line[j]
            if r != 0:
                L.append((m, j))
        top_line = mid_line
        mid_line = bot_line
        bot_line = f.readline().strip()
        m += 1

used = [[False] * n for _ in range(m)]

ans = 1
for _ in range(3):
    b = biggest_basin()
    y = 0
    for p in b:
        used[p[0]][p[1]] = True
        y += 1
    ans *= y

print("Answer = {}".format(ans))