#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:28:48 2021

@author: shavak
"""

a = 0.0
h = 0.0
d = 0.0
with open("input.txt", "r") as f:
    for line in f:
        s = line.split()
        u = float(s[1])
        if (s[0] == "forward"):
            h += u
            d += a * u
        elif (s[0] == "down"):
            a += u
        elif (s[0] == "up"):
            a -= u
            
print("Answer = {}".format(h * d))