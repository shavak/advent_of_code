#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:49:10 2021

@author: shavak
"""

top_line = ""
mid_line = ""
bot_line = ""

ans = 0

with open("input.txt", "r") as f:
    mid_line = f.readline().strip()
    bot_line = f.readline().strip()
    while mid_line != "":
        n = len(mid_line)
        for i in range(n):
            x = mid_line[i]
            r = 1 + int(mid_line[i])
            if i != 0:
                r *= x < mid_line[i - 1]
            if top_line != "":
                r *= x < top_line[i]
            if i != n - 1:
                r *= x < mid_line[i + 1]
            if bot_line != "":
                r *= x < bot_line[i]
            ans += r
        top_line = mid_line
        mid_line = bot_line
        bot_line = f.readline().strip()

print("Answer = {}".format(ans))