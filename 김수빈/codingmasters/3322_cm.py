# -*- coding: utf-8 -*-
import sys

def dfs_solution(N, relations, left, rows, i):
    if i == N: return 0
    
    max_score = None
    for j, y in enumerate(left):
        for k, x in enumerate(left[:j]):
            rows += [(x, y)]
            score = 0 if not (x, y) in relations else relations[(x, y)]
            score += dfs_solution(N, relations, left[:k] + left[k + 1:j] + left[j + 1:], rows, i + 1)
            max_score = score if max_score is None or score > max_score else max_score
    return max_score

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

rows = []
relations = {}
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    if b < c:
        relations[(b, c)] = a if a == 1 else -1
    else:
        relations[(c, b)] = a if a == 1 else -1

score = 0

print(dfs_solution(N, relations, list(range(1, 2 * N + 1)), rows, 0))