# -*- coding: utf-8 -*-
import sys

def solution(N, conds):
    temper = [0] * 30
    for s, e in conds:
        for i in range(s, e + 1):
            temper[i - 1] += 1
    
    return temper.index(max(temper)) + 1
    
N = int(sys.stdin.readline())
conds = list(sys.stdin.readlines())
conds = list(map(lambda x: tuple(map(int, x.split())), conds))

print(solution(N, conds))