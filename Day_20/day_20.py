#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:14:15 2022

@author: shavak
"""

input_file = "input.txt"
N = 50
A = ""
D = {}
x_min = 0
x_max = 0
y_min = 0
y_max = 0
infinite_light = False

def is_exterior(x, y):
    return x <= x_min or x >= x_max or y <= y_min or y >= y_max

def is_lit(x, y):
    if (x, y) in D:
        return True
    if infinite_light and is_exterior(x, y):
        return True
    return False

def algorithm_index(x, y):
    ans = 0
    for v in range(y + 1, y - 2, -1):
        for u in range(x - 1, x + 2):
            ans = 2 * ans + is_lit(u, v)
    return ans

def enhance_image():
    global D
    global x_min
    global x_max
    global y_min
    global y_max
    global infinite_light
    E = {}
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            i = algorithm_index(x, y)
            if A[i] == "#":
                E[(x, y)] = 1
    D = E
    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1
    if infinite_light:
        infinite_light = A[-1] == "#"
    else:
        infinite_light = A[0] == "#"
    
def num_lit_pixels():
    if infinite_light:
        return float("inf")
    return len(D)
    
with open(input_file, "r") as f:
    A = f.readline().strip()
    line = f.readline()
    line = f.readline()
    x = 0
    y = 0
    while line:
        l = len(line) - 1
        x = 0
        while x < l:
            if line[x] == '#':
                D[(x, y)] = 1
            x += 1
        y -= 1
        line = f.readline()
x_min = -1
x_max = x
y_min = y
y_max = 1
for i in range(N):
    enhance_image()
print("\nNumber of lit pixels = {}.".format(len(D)))