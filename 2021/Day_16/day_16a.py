#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:15:57 2022

@author: shavak
"""

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

def parse_packet(p):
    if len(p) < 11:
        # Simple (but not thorough) validation check.
        return 0
    ans = int(p[0 : 3], 2)
    t = int(p[3 : 6], 2)
    i = 0
    stack = []
    if t == 4:
        # Top-level packet represents a literal value. Easy peasy.
        return ans
    else:
        # Top-level packet represents an operator.
        if p[6] == '0':
            # The next 15 digits give the total length in bits of the
            # sub-packets contained in this operator packet.
            i = 22
            stack.append((i + int(p[7 : 22], 2), -1))
        else:
            # The next 11 bits are a number that represents the number of
            # sub-packets immediately contained in this operator packet.
            i = 18
            stack.append((-1, int(p[7 : 18], 2)))
    while stack:
        (k, m) = stack[-1]
        if i == k or m == 0:
            stack.pop()
            continue
        if m != -1:
            stack[-1] = (k, m - 1)
        # Right. Time to process a new packet.
        j = i
        i += 3
        ans += int(p[j : i], 2)
        t = int(p[i : i + 3], 2)
        i += 3
        if t == 4:
            # The packet that we're examining represents a literal value.
            while p[i] == '1':
                i += 5
            i += 5
        else:
            # The packet that we're examining represents an operator.
            if p[i] == '0':
                # The next 15 digits give the total length in bits of the
                # sub-packets contained in this operator packet.
                j = i + 1
                i += 16
                stack.append((i + int(p[j : i], 2), -1))
            else:
                # The next 11 bits are a number that represents the number of
                # sub-packets immediately contained in this operator packet.
                j = i + 1
                i += 12
                stack.append((-1, int(p[j : i], 2)))
    return ans 

with open(input_file, "r") as f:
    r = f.readline()
    packet = ""
    for i in range(len(r)):
        packet += hex_to_bin_map[r[i]]

print("Answer = {}.".format(parse_packet(packet)))