# -*- coding: utf-8 -*-
import sys

memo = {}
N = int(sys.stdin.readline())
for i in range(N):
    key, page = sys.stdin.readline().split()
    memo[key] = page

word = sys.stdin.readline().strip()
print(memo[word]) if word in memo else print(-1)