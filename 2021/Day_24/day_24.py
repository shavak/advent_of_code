#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:47:53 2022

@author: shavak
"""

input_file = "input.txt"

op_map = {
    "add" : lambda a, b : a + b,
    "mul" : lambda a, b : a * b,
    "div" : lambda a, b : a // b,
    "mod" : lambda a, b : a % b,
    "eql" : lambda a, b : 1 if a == b else 0
    }

registers = ["w", "x", "y", "z"]

def alu_helper(subprogram, z_dict, f):
    m = len(subprogram)
    res = {}
    for t in [(w, x, y, z)
              for w in range(9, 0, -1)
              for x in [0]
              for y in [0]
              for z in z_dict.keys()]:
        R = {registers[k] : t[k] for k in range(4)}
        for i in range(1, m):
            tokens = subprogram[i].split()
            if tokens[2] in R:
                R[tokens[1]] = op_map[tokens[0]](R[tokens[1]], R[tokens[2]])
            else:
                R[tokens[1]] = op_map[tokens[0]](R[tokens[1]], int(tokens[2]))
        h = 10 * z_dict[t[3]] + t[0]
        if R["z"] in res:
            res[R["z"]] = f(res[R["z"]], h)
        else:
            res[R["z"]] = h
    return res

def constrained_model_number(program, f):
    p = 0
    z_dict = {0 : 0}
    q = 1
    n = len(program)
    while q < n:
        instr = program[q].split()[0]
        if instr == "inp":
            z_dict = alu_helper(program[p : q], z_dict, f)
            p = q
        q += 1
    z_dict = alu_helper(program[p : n], z_dict, f)
    return z_dict[0] if 0 in z_dict else None

with open(input_file, "r") as file_handler:
    program = file_handler.readlines()

print("\nAnswer = {}.".format(constrained_model_number(program, min)))