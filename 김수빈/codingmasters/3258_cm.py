# -*- coding: utf-8 -*-
import sys

left, right = 0, 0
table = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]

N = int(sys.stdin.readline())
for i in range(N):
    l, r = map(int, sys.stdin.readline().split())
    score = table[l - 1][r - 1]
    if score < 0:
        right += 1
    elif score > 0:
        left += 1
        
print(f"{left} {right}")