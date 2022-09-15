# -*- coding: utf-8 -*-
import sys

def solution(N):
    if N <= 0: return []
    if N == 1: return ['*']

    prev = solution(N - 1)
    rows = []
    rows += [pr + ' '* len(pr) + pr for pr in prev]
    rows += [' '* len(pr) + pr + ' '* len(pr) for pr in prev]
    rows += [pr + ' '* len(pr) + pr for pr in prev]

    return rows

N = int(sys.stdin.readline())
answer = '\n'.join(solution(N))
print(answer)