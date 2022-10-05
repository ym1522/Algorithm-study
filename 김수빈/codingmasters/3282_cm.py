# -*- coding: utf-8 -*-
import sys
import numpy as np

def padding(board, N, M, pad):
    padded = np.zeros((N + 2 * pad, M + 2 * pad))
    padded[pad:pad + N, pad:pad + M] = board
    return padded

N, M = map(int, sys.stdin.readline().split())
board = np.array(list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines())))
board = padding(board, N, M, pad=1)
max_val = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        val = board[i][j] + board[i-1][j] + board[i][j-1] + board[i][j+1]+ board[i+1][j]
        max_val = val if val > max_val else max_val
print(int(max_val))