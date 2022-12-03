#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:46:00 2022

@author: shavak
"""

input_file = "input.txt"

m = 0
n = 0
E = {}
S = {}

def step():
    global m
    global n
    global E
    global S
    ans = True
    M = {}
    for (i, j) in E:
        k = (j + 1) % n
        if (i, k) not in E and (i, k) not in S:
            M[(i, j)] = (i, k)
    for (i, j) in M.keys():
        E.pop((i, j))
        E[M[(i, j)]] = True
        ans = False
    M.clear()
    for (i, j) in S:
        k = (i + 1) % m
        if (k, j) not in E and (k, j) not in S:
            M[(i, j)] = (k, j)
    for (i, j) in M.keys():
        S.pop((i, j))
        S[M[(i, j)]] = True
        ans = False
    return ans

with open(input_file, "r") as file_handler:
    for line in file_handler.readlines():
        row = line.strip()
        n = len(row)
        for j in range(n):
            if row[j] == ">":
                E[(m, j)] = True
            if row[j] == "v":
                S[(m, j)] = True
        m += 1

stationary = False
s = 0
while not stationary:
    s += 1
    stationary = step()

print("\nAnswer = {}.".format(s))