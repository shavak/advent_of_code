#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:42:19 2022

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

pos_map = {
    "w" : 0,
    "x" : 1,
    "y" : 2,
    "z" : 3
    }

instruction_map = {
    "add" : "+",
    "mul" : "*",
    "div" : "//",
    "mod" : "%",
    }

register_map = {
    "w" : 0,
    "x" : 1,
    "y" : 2,
    "z" : 3
    }

N = 14

def maximum_model_number_lite(program):
    # For this version, I'm going to assume that all inputs come to into w.
    n = len(program)
    stack = [[{0 : 0}, 0, 0, 0, 0]]
    ans = 0
    while stack:
        state = stack.pop()
        w = state[0]
        p = state[4]
        if p == n:
            if state[pos_map["z"]] == 0:
                ans = max(ans, max([w[k] for k in w]))
            continue
        tokens = program[p].split()
        op_str = tokens[0]
        if op_str == "inp":
            c = 10 * max(w.values())
            w_new = {}
            for j in range(1, 10):
                w_new[j] = c + j
            stack.append([w_new] + state[1 : 4] + [p + 1])
        else:
            op = op_map[op_str]
            foo = tokens[1]
            bar = tokens[2]
            if foo == "w":
                if bar == "w":
                    g = {}
                    for k in w:
                        u = op(w[k], w[k])
                        if u not in g:
                            g[u] = [k]
                        else:
                            g[u].append(k)
                    w_new = {u : max([w[k] for k in g[u]]) for u in g}
                    state_new = [None] * 5
                    state_new[pos_map[foo]] = w_new
                    for j in range(1, 4):
                        state_new[j] = state[j]
                    state_new[4] = p + 1
                    stack.append(state_new)
                else:
                    w_new = {}
                    b = state[pos_map[bar]] if bar in pos_map else int(bar)
                    for k in w:
                        w_new[op(k, b)] = w[k]
                stack.append([w_new] + state[1 : 4] + [p + 1])
            elif bar == "w":
                # This is the tricky part. I'm forced to branch here.
                q = state[pos_map[foo]]
                g = {}
                for k in w:
                    u = op(q, w[k])
                    if u not in g:
                        g[u] = [k]
                    else:
                        g[u].append(k)
                for u in g:
                    state_new = [None] * 5
                    w_new = {}
                    for k in g[u]:
                        w_new[k] = w[k]
                    state_new[pos_map["w"]] = w_new
                    for j in range(1, 5):
                        state_new[j] = state[j]
                    state_new[pos_map[foo]] = u
                    state_new[4] += 1
                    stack.append(state_new)
            else:
                state_new = [None] * 5
                state_new[pos_map["w"]] = w
                for j in range(1, 4):
                    state_new[j] = state[j]
                state_new[4] = p + 1
                b = state[pos_map[bar]] if bar in pos_map else int(bar)
                j = pos_map[foo]
                state_new[j] = op(state[j], b)
                stack.append(state_new)
    return ans

def maximum_model_number2(program):
    n = len(program)
    S = {(0, 0, 0, 0) : 0}
    for i in range(n):
        tokens = program[i].split()
        S_new = {}
        if tokens[0] == "inp":
            for k in S:
                for j in range(1, 10):
                    l = list(k)
                    l[pos_map[tokens[1]]] = j
                    c = 10 * S[k] + j
                    q = tuple(l)
                    if q in S_new:
                        S_new[q] = max(c, S_new[q])
                    else:
                        S_new[q] = c
        else:
            for k in S:
                l = list(k)
                u = pos_map[tokens[1]]
                t = tokens[2]
                b = k[pos_map[t]] if t in pos_map else int(t)
                l[u] = op_map[tokens[0]](k[u], b)
                S_new[tuple(l)] = S[k]
        S = S_new
    ans = 0
    u = pos_map["z"]
    for k in S:
        if k[u] == 0:
            ans = max(ans, S[k])
    return ans

def alu_exec(subprogram, S):
    w, x, y, z = S
    locals_dict = {"w" : w, "x" : x, "y" : y, "z" : z}
    for i in range(len(subprogram)):
        line = subprogram[i].split()
        if line[0] == "eql":
            exec(f"{line[1]} = 1 if {line[1]} == {line[2]} else 0",
                 globals(), locals_dict)
        else:
            exec(f"{line[1]} = {line[1]} {instruction_map[line[0]]} {line[2]}",
                 globals(), locals_dict)
        w = locals_dict["w"]
        x = locals_dict["x"]
        y = locals_dict["y"]
        z = locals_dict["z"]
    return w, x, y, z


def largest_model_number(X):
    ans = 0
    for i in range(len(X) - 1, -1, -1):
        ans *= 10
        ans += max(X[i])
    return ans

with open(input_file, "r") as file_handler:
    program = file_handler.readlines()

def dependent_variables(subprogram):
    m = len(subprogram)
    D = {}
    if m == 0:
        return D
    line = subprogram[0].split()
    a = line[1]
    D[a] = 1
    for i in range(1, m):
        line = subprogram[i].split()
        a = line[1]
        b = line[2]
        if b in D:
            D[a] = 1
    return D

def preprocess(program, l):
    program_copy = program.copy()
    m = len(program)
    i = -1
    res = []
    for j in range(m):
        line = program[j].split()
        if line[0] == "inp":
            if i >= 0:
                D = dependent_variables(program[i : j])
                if "z" in D:
                    res.append(0)
                else:
                    program_copy[j] = "set " + line[1] + " " + str(l) + "\n"
                    res.append(l)
            i = j
    return res, program_copy

def maximum_model_number(program, k, l):
    R = {"w" : 0, "x" : 0, "y" : 0, "z" : 0}
    S = {}
    stack = []
    N = len(program)
    p = 0
    while p < N:
        line = program[p].split()
        instruction = line[0]
        a = line[1]
        if instruction == "inp":
            if p in S:
                if S[p][a] == k:
                    S.pop(p)
                    stack.pop()
                    if not stack:
                        return None
                    else:
                        p = stack[-1][0]
                        R = S[p].copy()
                        continue
                else:
                    R[a] -= 1
                    S[p][a] -= 1
            else:
                R[a] = l
                S[p] = R.copy()
                stack.append((p, a))
        else:
            b = line[2]
            f = op_map[instruction]
            if b in R:
                R[a] = f(R[a], R[b])
            else:
                b = int(b)
                R[a] = f(R[a], b)
        if p == N - 1:
            if R["z"] == 0:
                ans = 0
                m = len(stack)
                for i in range(m):
                    u, v = stack[i]
                    ans *= 10
                    ans += S[u][v]
                return ans
            else:
                if not stack:
                    return None
                else:
                    p = stack[-1][0]
                    R = S[p].copy()
                    continue 
        p += 1
    return None

def input_dependency(program):
    res = {"w" : {}, "x" : {}, "y" : {}, "z" : {}}
    N = len(program)
    for i in range(N):
        tokens = program[i].split()
        if tokens[0] == "inp":
            res[tokens[1]] = {i : True}
        elif tokens[0] == "mul" and tokens[2] == 0:
            res[tokens[1]] = {}
        elif tokens[2] in res:
            temp_dict = {}
            for k in res[tokens[1]].keys():
                temp_dict[k] = True
            for k in res[tokens[2]].keys():
                temp_dict[k] = True
            res[tokens[1]] = temp_dict
    return res

def input_check(program):
    N = len(program)
    for i in range(N):
        tokens = program[i].split()
        if tokens[0] == "inp" and tokens[1] != "w":
            print("AAAARGGHHHHH!")
    
X = model_number_generator(program)
print("\nAnswer = {}.".format(largest_model_number(X)))