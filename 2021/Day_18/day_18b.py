#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 16:20:25 2022

@author: shavak
"""

import numpy as np

input_file = "input.txt"

def snailfish_number(x):
    a = []
    i = 0
    n = len(x)
    while i < n:
        if x[i] == " ":
            i += 1
        elif x[i] == "[" or x[i] == "]" or x[i] == ",":
            a.append(x[i])
            i += 1
        elif x[i] == "\n":
            break
        else:
            s = ""
            while x[i].isdigit():
                s += x[i]
                i += 1
            a.append(int(s))
    return a

def snailfish_explode(x):
    a = x.copy()
    n = len(a)
    j = 0
    nest_count = 0
    b = 0
    k = []
    while j < n:
        if a[j] == "[":
            nest_count += 1
        elif type(a[j]) == int:
            a[j] += b
            b = 0
            k.append(j)
        elif a[j] == "]":
            nest_count -= 1
            if nest_count >= 4:
                k.pop()
                k.pop()
                if k:
                    a[k[-1]] += a[j - 3]
                b = a[j - 1]
                j -= 4
                k.append(j)
                a = [*a[0 : j], *[0], *a[j + 5 : n]]
                n -= 4 
        j += 1
    return a

def snailfish_reduce(x):
    a = snailfish_explode(x)
    n = len(a)
    j = 0
    nest_count = 0
    while j < n:
        incr = True
        if a[j] == "[":
            nest_count += 1
            if nest_count > 4:
                a = snailfish_explode(a)
                n = len(a)
                j = 0
                nest_count = 0
                incr = False
        elif type(a[j]) == int:
            if a[j] >= 10:
                s = a[j] // 2
                a = [*a[0 : j], *["[", s, ",", s + (a[j] % 2), "]"],\
                     *a[j + 1 : n]]
                n += 4
                incr = False
        elif a[j] == "]":
            nest_count -= 1
        j += incr
    return a

def snailfish_sum(x, y):
    if x == []:
        return y
    a = [*["["], *x, *[","], *y, *["]"]]
    return snailfish_reduce(a)

def snailfish_magnitude(x):
    acc = []
    for c in x:
        if type(c) == int:
            acc.append(c)
        if c == "]":
            # Action Jackson.
            s = 2 * acc.pop() + 3 * acc.pop()
            acc.append(s)
    return acc[0]

def snailfish_string(x):
    s = ""
    for r in x:
        s += str(r) if type(r) == int else r
    return s

def max_pairwise_sum(Z):
    ans = -np.infty
    m = len(Z)
    for i in range(m):
        for j in range(m):
            ans = max(ans, snailfish_magnitude(snailfish_sum(Z[i], Z[j])))
    return ans

with open(input_file, "r") as f:
    Z = []
    for row in f:
        Z.append(snailfish_number(row))
        
print("\nAnswer = {}.".format(max_pairwise_sum(Z)))
