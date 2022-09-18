 # -*- coding: utf-8 -*-
import sys

N, M = map(int, sys.stdin.readline().split())
board = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

max_val = 0
for i in range(0, N):
    for j in range(0, M):
        val = board[i][j]
        if i - 1 >= 0:
            val += board[i - 1][j]
        if j - 1 >= 0:
            val += board[i][j - 1]
        if i + 1 < N:
            val += board[i + 1][j]
        if j + 1 < M:
            val += board[i][j + 1]
        max_val = val if val > max_val else max_val
print(max_val)