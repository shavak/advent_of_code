#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:21:29 2022

@author: shavak
"""

import numpy as np

num_steps = 10

rules = {}
count = {}

with open("input.txt", "r") as f:
    polymer = f.readline().strip()
    for elt in polymer:
        if elt not in count.keys():
            count[elt] = 1
        else:
            count[elt] += 1
    f.readline()
    line = f.readline()
    while line != "":
        r = [x.strip() for x in line.split("->")]
        rules[r[0]] = r[1]
        line = f.readline()

for i in range(num_steps):
    new_polymer = polymer[0]
    for j in range(1, len(polymer)):
        elt2 = polymer[j - 1 : j + 1]
        if elt2 in rules.keys():
            elt = rules[elt2]
            if elt not in count.keys():
                count[elt] = 1
            else:
                count[elt] += 1
            new_polymer += elt
        new_polymer += polymer[j]
    polymer= new_polymer

min_count = np.inf
max_count = -np.inf 
for k in count.keys():
    if count[k] < min_count:
        min_count = count[k]
    if count[k] > max_count:
        max_count = count[k]

print("Answer = {}".format(max_count - min_count))
    
            