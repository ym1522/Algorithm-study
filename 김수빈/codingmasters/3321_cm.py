# -*- coding: utf-8 -*-
import sys
N, M = map(int, sys.stdin.readline().split())
visiting = list(map(lambda x: tuple(map(lambda k: tuple(map(int, k.split(":"))), x.split())), sys.stdin.readlines()))

state = []
visiting = sorted(visiting, key=lambda x: x[0])

cnt = 0
for s, e in visiting:
    state = list(filter(lambda x: x[1] > s, state))
    if not state or len(state) < N: 
        state += [(s, e)]
        cnt += 1
print(cnt)