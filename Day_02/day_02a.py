#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:15:34 2021

@author: shavak
"""

p = {"forward" : 0, "down" : 0, "up" : 0}
with open("input.txt", "r") as f:
    for line in f:
        x = line.split()
        p[x[0]] += float(x[1])
print("Answer = {}".format(p["forward"] * (p["down"] - p["up"])))