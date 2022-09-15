# -*- coding: utf-8 -*-
import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

cands = [B[i:] + B[:i] for i in range(len(B))]
print('YES') if A in cands else print("NO")