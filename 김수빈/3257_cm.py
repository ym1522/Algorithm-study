# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
for i in range(max(N, 3), N * 3 + 1):
    if i % N == 0 and i % 3 == 0:
        print(i)
        break