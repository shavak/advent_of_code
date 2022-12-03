#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:54:53 2022

@author: shavak
"""

closes = [")", "]", "}", ">"]
parens = dict(zip(closes, ["(", "[", "{", "<"]))
points = dict(zip(closes, [3, 57, 1197, 25137]))

score = 0
with open("input.txt", "r") as f:
    for line in f:
        stack = []
        for x in line.strip():
            if x in parens.keys():
                if not stack:
                    score += points[x]
                    break
                elif stack.pop() != parens[x]:
                    score += points[x]
                    break
            else:
                stack.append(x)

print("Answer = {}".format(score))