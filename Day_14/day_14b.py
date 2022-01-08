#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:03:21 2022

@author: shavak
"""

import numpy as np

num_steps = 40

rules = {}
single_count = {}
pair_count = {}

with open("input.txt", "r") as f:
    polymer = f.readline().strip()
    n = len(polymer)
    if n > 0:
        single_count[polymer[0]] = 1
    for j in range(1, len(polymer)):
        elt = polymer[j]
        if elt not in single_count.keys():
            single_count[elt] = 1
        else:
            single_count[elt] += 1
        elt2 = polymer[j - 1 : j + 1]
        if elt2 not in pair_count.keys():
            pair_count[elt2] = 1
        else:
            pair_count[elt2] += 1
    f.readline()
    line = f.readline()
    while line != "":
        r = [x.strip() for x in line.split("->")]
        rules[r[0]] = r[1]
        line = f.readline()

for i in range(num_steps):
    new_pair_count = {}
    for y in pair_count.keys():
        if y in rules.keys():
            m = pair_count[y]
            x = rules[y]
            z = y[0] + x
            if z not in new_pair_count.keys():
                new_pair_count[z] = m
            else:
                new_pair_count[z] += m
            z = x + y[1]
            if z not in new_pair_count.keys():
                new_pair_count[z] = m
            else:
                new_pair_count[z] += m
            if x not in single_count.keys():
                single_count[x] = m
            else:
                single_count[x] += m
    pair_count = new_pair_count
    

min_count = np.inf
max_count = -np.inf 
for k in single_count.keys():
    if single_count[k] < min_count:
        min_count = single_count[k]
    if single_count[k] > max_count:
        max_count = single_count[k]

print("Answer = {}".format(max_count - min_count))