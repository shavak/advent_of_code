#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 06:41:56 2021

@author: shavak
"""

# For this problem, I'm forced to assume that the binary numbers on each line
# of the input file are of the same length. The operation is not well-defined
# otherwise.

# Also, the given procedure is not guaranteed to terminate and, even if it
# does, it is not guaranteed to terminate with only one number remaining.
# The code below is robust to this, in that it will always choose the number
# that comes first in the input list in case of ambiguity.

def mode_filter(x, n, oxygen = True):
    m = len(x)
    u = list(range(m))
    k = n - 1
    while (m > 1) and (k >= 0):
        v = [[], []]
        for i in range(m):
            j = u[i]
            v[(x[j] & (1 << k)) >> k].append(j)
        q = [len(v[0]), len(v[1])]
        b = oxygen == 1
        if q[0] > q[1]:
            b = oxygen == 0    
        if (q[b] == 0):
            break
        u = v[b]
        m = q[b]
        k -= 1
    return x[u[0]]

f = open("input.txt", "r")
line = f.readline()
n = len(line) - 1
y = []
while line != "":
    y.append(int(line, 2))
    line = f.readline()
f.close()        
print("Answer = {}".format(
    mode_filter(y, n, oxygen = True) * mode_filter(y, n, oxygen = False)))
            