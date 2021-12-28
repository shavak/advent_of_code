#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:04:15 2021

@author: shavak
"""

# For this problem, I'm forced to assume that the binary numbers on each line
# of the input file are of the same length. The operation is not well-defined
# otherwise.

f = open("input.txt", "r")
line = f.readline()
n = len(line) - 1
c = [0 for _ in range(n)]
m = 0

while line != "":
    m += 1
    for i in range(n):
        c[i] += (line[i] == '1')
    line = f.readline()

h = m / 2
g = 0
e = 0
for i in range(n):
    x = c[i] > h
    g = 2 * g + x
    e = 2 * e + (1 - x)

print("Answer = {}".format(g * e))