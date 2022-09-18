# -*- coding: utf-8 -*-
import sys

password = sys.stdin.readline().strip()
N = len(password)
for i in range(1, N + 1):
    if N % i != 0: continue
    if (password[:i]) * (N // i) == password:
        print(password[:i])
        break