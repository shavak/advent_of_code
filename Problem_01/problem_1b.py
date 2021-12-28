#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:22:33 2021

@author: shavak
"""

from queue import Queue

N = 3

q = Queue(maxsize = N)
s = 0.0
c = 0
line = ""
f = open("input.txt", "r")

for i in range(N):
    line = f.readline()
    if line == "":
        break
    else:
        x = float(line)
        q.put(x)
        s += x

line = f.readline()
while line != "":
    x = float(line)
    t = s - q.get() + x
    q.put(x)
    c += (t > s)
    s = t
    line = f.readline()

f.close()

print("Answer = {}".format(c))