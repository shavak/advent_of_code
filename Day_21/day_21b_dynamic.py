#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 02:04:53 2022

@author: shavak
"""

input_file = "input.txt"

M = 21
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

def dirac_tables():
    D = dirac_dice_roll_3()
    N = M + 1
    A1 = [[] for q in range(N)]
    B1 = [[] for q in range(N)]
    A2 = [[] for q in range(N)]
    B2 = [[] for q in range(N)]
    for q in range(1, N):
        A1[q] = [[[0 for j in range(k)] for i in range(k)] for s in range(q)]
        B1[q] = [[[0 for j in range(k)] for i in range(k)] for s in range(q)]
        A2[q] = [[[0 for j in range(k)] for i in range(k)] for s in range(q)]
        B2[q] = [[[0 for j in range(k)] for i in range(k)] for s in range(q)]
    for i in range(k):
        for j in range(k):
            A1[1][0][i][j] = 27
            B1[1][0][i][j] = 27
    for q in range(2, N):
        for s in range(q):
            for i in range(k):
                for j in range(k):
                    # I've split out each of the table updates for clarity.
                    # They can be amalgamated to yield a small speed-up.
                    # Update A1.
                    for x in D:
                        g = (i + x) % k
                        u = k if g == 0 else g
                        t = s + u
                        if t >= q:
                            A1[q][s][i][j] += D[x]
                            continue
                        for y in D:
                            h = (j + y) % k
                            v = k if h == 0 else h
                            z = D[x] * D[y]
                            if v >= q:
                                continue
                            elif t > v:
                                A1[q][s][i][j] += z * A1[q - v][t - v][g][h]
                            else:
                                A1[q][s][i][j] += z * B1[q - t][v - t][g][h]
                    # Update B1.
                    for x in D:
                        g = (i + x) % k
                        u = k if g == 0 else g
                        if u >= q:
                            B1[q][s][i][j] += D[x]
                            continue
                        for y in D:
                            h = (j + y) % k
                            v = k if h == 0 else h
                            t = s + v
                            z = D[x] * D[y]
                            if t >= q:
                                continue
                            elif t > u:
                                B1[q][s][i][j] += z * B1[q - u][t - u][g][h]
                            else:
                                B1[q][s][i][j] += z * A1[q - t][u - t][g][h]
                    # Update A2.
                    for x in D:
                        g = (i + x) % k
                        u = k if g == 0 else g
                        t = s + u
                        if t >= q:
                            continue
                        for y in D:
                            h = (j + y) % k
                            v = k if h == 0 else h
                            z = D[x] * D[y]
                            if v >= q:
                                A2[q][s][i][j] += z
                            elif t > v:
                                A2[q][s][i][j] += z * A2[q - v][t - v][g][h]
                            else:
                                A2[q][s][i][j] += z * B2[q - t][v - t][g][h]
                    # Update B2.
                    for x in D:
                        g = (i + x) % k
                        u = k if g == 0 else g
                        if u >= q:
                            continue
                        for y in D:
                            h = (j + y) % k
                            v = k if h == 0 else h
                            t = s + v
                            z = D[x] * D[y]
                            if t >= q:
                                B2[q][s][i][j] += z
                            elif t > u:
                                B2[q][s][i][j] += z * B2[q - u][t - u][g][h]
                            else:
                                B2[q][s][i][j] += z * A2[q - t][u - t][g][h]
    return A1, B1, A2, B2

with open(input_file, "r") as f:
    i = int(f.readline().split(": ")[1])
    j = int(f.readline().split(": ")[1])

A1, B1, A2, B2 = dirac_tables()
print("\nAnswer = {}.".format(max(A1[M][0][i][j], A2[M][0][i][j])))