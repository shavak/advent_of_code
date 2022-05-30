#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:28:22 2022

@author: shavak
"""

import numpy as np

overlap_threshold = 12

input_file = "input.txt"

U = []
S = {}
B = {}
C = {}

def transformation_matrix():
    facing = [np.identity(3, dtype = int),
              np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]], dtype = int),
              np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype = int),
              np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], dtype = int),
              np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype = int),
              np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]], dtype = int)]
    A = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype = int)
    up = [np.identity(3, dtype = int)]
    for _ in range(3):
        up.append(np.matmul(up[-1], A))
    return np.concatenate([np.matmul(U, F) for F in facing for U in up],
                          axis = 0)

def num_common_beacons(E, H):
    D = {tuple(E[:, j]) : 1 for j in range(E.shape[1])}
    ans = 0
    for j in range(H.shape[1]):
        if tuple(H[:, j]) in D:
            ans += 1
    return ans

def detect_overlap_helper(E, G):
    l = E.shape[1]
    m = G.shape[1]
    for j in range(l):
        for k in range(m):
            x = (E[:, j] - G[:, k]).reshape((3, 1))
            H = G + x
            if num_common_beacons(E, H) >= overlap_threshold:
                return x, H
    return None, None 

def detect_overlap(E, F):
    for i in range(0, 72, 3):
        x, H = detect_overlap_helper(E, F[i : i + 3, :])
        if x is not None:
            return True, x, H
    return False, x, H

def process_scanner(p):
    global U
    global S
    global B
    global C
    for k in S.keys():
        success, x, A = detect_overlap(B[k], U[p])
        if success:
            S[p] = x
            B[p] = A
            for j in range(A.shape[1]):
                t = tuple(A[:, j])
                if t in C:
                    C[t] += 1
                else:
                    C[t] = 1
            return True
    return False

def map_beacons():
    global U
    global S
    global B
    global C
    n = len(U)
    if n == 0:
        # No scanners to process.
        return
    S[0] = np.zeros((3, 1), dtype = int)
    B[0] = U[0][0 : 3, :]
    for j in range(B[0].shape[1]):
        C[tuple(B[0][:, j])] = 1
    Q = [False for _ in range(n)]
    p = 1
    w = n - 1
    Q[0] = True
    while w > 0:
        # Find a scanner to process.
        while Q[p] == True:
            p = (p + 1) % n
        if process_scanner(p):
            Q[p] = True
            w -= 1
        p = (p + 1) % n

def largest_manhattan_distance_scanners():
    ans = -np.inf
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, np.sum(np.abs(S[i] - S[j])))
    return ans

def read_scanner_data():
    global U
    X = []
    T = transformation_matrix()
    with open(input_file, "r") as f:
        for line in f.readlines():
            if "scanner" in line:
                X = []
                continue
            elif line == "\n":
                U.append(np.matmul(T, np.transpose(np.array(X, dtype = int))))
                continue
            else:
                X.append([int(e) for e in line.strip().split(",")])
    U.append(np.matmul(T, np.transpose(np.array(X, dtype = int))))

read_scanner_data()
map_beacons()
print("\nNumber of beacons = {}.".format(len(C)))
print("\nMaximum Manhattan distance between scanners = {}."\
      .format(largest_manhattan_distance_scanners()))