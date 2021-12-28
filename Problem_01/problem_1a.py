#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:39:05 2021

@author: shavak
"""

x = float("inf")
c = 0
with open("input.txt", "r") as f:
    for line in f:
        y = float(line)
        c += (y > x)
        x = y
print("Answer = {}".format(c))