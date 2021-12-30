#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 18:19:36 2021

@author: shavak
"""

Z = ["a", "b", "c", "d", "e", "f", "g"]

D = {"abcefg" : 0,
     "cf" : 1,
     "acdeg" : 2,
     "acdfg" : 3,
     "bcdf" : 4,
     "abdfg" : 5,
     "abdefg" : 6,
     "acf" : 7,
     "abcdefg" : 8,
     "abcdfg" : 9}

def decode_segment_labels(p):
    F = {6 : "b", 4 : "e", 9 : "f", 7 : None, 8: None}
    N = {v : 0 for v in Z}
    for x in [s for q in p for s in q]:
        N[x] += 1
    M = {v : None for v in Z}
    for x in N.keys():
        M[x] = F[N[x]]
    # At this point the map is almost half complete!
    L = {i : None for i in range(2, 8)}
    for s in p:
        L[len(s)] = s
    if M[L[2][0]] == "f":
        M[L[2][1]] = "c"
    else:
        M[L[2][0]] = "c"
    for x in L[3]:
        if x not in L[2]:
            M[x] = "a"
            break
    for x in L[4]:
        if M[x] == None:
            M[x] = "d"
            break
    for x in L[7]:
        if M[x] == None:
            M[x] = "g"
    return M

ans = 0
with open("input.txt", "r") as f:
    for line in f:
        reading = line.split("|")
        p = reading[0].split()
        M = decode_segment_labels(p)
        m = 0
        for s in reading[1].split():
            m = 10 * m + D["".join(sorted([M[x] for x in s]))]
        ans += m

print("Answer = {}".format(ans))