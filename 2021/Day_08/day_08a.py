#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:06:27 2021

@author: shavak
"""

U = {2 : [1], 3 : [7], 4 : [4], 7 : [8]}

with open("input.txt", "r") as f:
    print("Answer = {}".format(sum([len(s.strip()) in U.keys()
                                    for line in f
                                    for s in line.split("|")[1].split()])))