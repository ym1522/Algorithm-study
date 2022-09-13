# -*- coding: utf-8 -*-
import sys

N, A = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
touches = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))
zombi = [A]
for i, j in touches:
    if i in zombi or j in zombi:
        zombi += [i, j]
print(len(set(zombi)))