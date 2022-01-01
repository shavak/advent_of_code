#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 15:48:01 2022

@author: shavak
"""

opens = ["(", "[", "{", "<"]
closes = [")", "]", "}", ">"]
parens = dict(zip(closes, ["(", "[", "{", "<"]))
points = dict(zip(opens, [1, 2, 3, 4]))

scores = []
stack = []
with open("input.txt", "r") as f:
    for line in f:
        s = 0
        incomplete = True
        for x in line.strip():
            if x in parens.keys():
                if not stack:
                    incomplete = False
                    break
                elif stack.pop() != parens[x]:
                    incomplete = False
                    stack.clear()
                    break
            else:
                stack.append(x)
        while stack:
            s = 5 * s + points[stack.pop()]
        if incomplete:    
            scores.append(s)

# I'm sorting because the problem has asked for this, but the median can of
# course be found in O(n) time.            
print("Answer = {}".format(sorted(scores)[(len(scores) - 1) // 2]))