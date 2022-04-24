#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:16:07 2022

@author: shavak
"""

import operator
from functools import reduce

input_file = "input.txt"

hex_to_bin_map = {
    "\n" : "",
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
    }

op_map = {
    0 : sum,
    1 : lambda x : reduce(operator.mul, x),
    2 : min,
    3 : max,
    5 : lambda x : 1 if x[0] > x[1] else 0,
    6 : lambda x : 1 if x[0] < x[1] else 0,
    7 : lambda x : 1 if x[0] == x[1] else 0
    }

def evaluate_literal(p, i):
    ans_str = ""
    while p[i] == '1':
        j = i + 5
        ans_str += p[i + 1 : j]
        i = j
    j = i + 5
    ans_str += p[i + 1 : j]
    return int(ans_str, 2), j
    

def evaluate_packet(p):
    if len(p) < 11:
        # Simple (but not thorough) validation check.
        return 0
    t = int(p[3 : 6], 2)
    i = 0
    stack = []
    if t == 4:
        # Top-level packet represents a literal value. Easy peasy.
        return evaluate_literal(p, 7)
    else:
        # Top-level packet represents an operator.
        if p[6] == '0':
            # The next 15 digits give the total length in bits of the
            # sub-packets contained in this operator packet.
            i = 22
            stack.append([t, i + int(p[7 : 22], 2), -1, []])
        else:
            # The next 11 bits are a number that represents the number of
            # sub-packets immediately contained in this operator packet.
            i = 18
            stack.append([t, -1, int(p[7 : 18], 2), []])
    a = None
    while stack:
        s = stack[-1]
        if a is not None:
            s[3].append(a)
        if i == s[1] or s[2] == 0:
            a = op_map[s[0]](s[3])
            stack.pop()
            continue
        if s[2] != -1:
            s[2] -= 1
        # Right. Time to process a new packet.
        j = i
        i += 3
        t = int(p[i : i + 3], 2)
        i += 3
        if t == 4:
            # The packet that we're examining represents a literal value.
            a, i = evaluate_literal(p, i)
        else:
            # The packet that we're examining represents an operator.
            a = None
            if p[i] == '0':
                # The next 15 digits give the total length in bits of the
                # sub-packets contained in this operator packet.
                j = i + 1
                i += 16
                stack.append([t, i + int(p[j : i], 2), -1, []])
            else:
                # The next 11 bits are a number that represents the number of
                # sub-packets immediately contained in this operator packet.
                j = i + 1
                i += 12
                stack.append([t, -1, int(p[j : i], 2), []])
    return a 

with open(input_file, "r") as f:
    r = f.readline()
    packet = ""
    for i in range(len(r)):
        packet += hex_to_bin_map[r[i]]

print("Answer = {}.".format(evaluate_packet(packet)))