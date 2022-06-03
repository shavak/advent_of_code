#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:51:29 2022

@author: shavak
"""

input_file = "test_input2.txt"

on_cuboids = []

def interval_intersection(I, J):
    p = 0
    q = 0
    if J[0] >= I[0] and J[0] <= I[1]:
        p = J[0]
        q = min(I[1], J[1])
    elif I[0] >= J[0] and I[0] <= J[1]:
        p = I[0]
        q = min(I[1], J[1])
    else:
        return None
    return [p, q]

def hypercuboid_intersection(A, B):
    ans = []
    n = len(A)
    for k in range(n):
        I = interval_intersection(A[k], B[k])
        if I == None:
            return None
        else:
            ans.append(I)
    return ans

def cuboidectomy(A, R):
    ans = []
    x1 = R[0][0] - 1
    x2 = R[0][1] + 1
    if A[0][0] <= x1:
        ans.append([[A[0][0], x1]] + A[1 : ])
    if x2 <= A[0][1]:
        ans.append([[x2, A[0][1]]] + A[1 : ])
    y1 = R[1][0] - 1
    y2 = R[1][1] + 1
    if A[1][0] <= y1:
        ans.append([R[0], [A[1][0], y1], A[2]])
    if y2 <= A[1][1]:
        ans.append([R[0], [y2, A[1][1]], A[2]])
    z1 = R[2][0] - 1
    z2 = R[2][1] + 1
    if A[2][0] <= z1:
        ans.append(R[0 : 2] + [[A[2][0], z1]])
    if z2 <= A[2][1]:
        ans.append(R[0 : 2] + [[z2, A[2][1]]])
    return ans

def add_cuboid(Q, switch_on):
    global on_cuboids
    if not on_cuboids and switch_on:
        on_cuboids.append(Q)
        return
    on_cuboids_new = []
    for U in on_cuboids:
        R = hypercuboid_intersection(U, Q)
        on_cuboids_new.extend(cuboidectomy(U, R))
        if switch_on:
            on_cuboids_new.extend(cuboidectomy(Q, R) + [R])
    on_cuboids = on_cuboids_new
    
def number_on_cubes():
    ans = 0
    for Q in on_cuboids:
        ans += (Q[0][1] - Q[0][0] + 1) * (Q[1][1] - Q[1][0] + 1)\
            * (Q[2][1] - Q[2][0] + 1)
    return ans
    
with open(input_file, "r") as f:
    for line in f.readlines():
        flip, coords = line.split()
        Q = [[int(c) for c in u[2 : ].split("..")] for u in coords.split(",")]
        add_cuboid(Q, flip == "on")
            
print("\nAnswer = {}.".format(number_on_cubes()))