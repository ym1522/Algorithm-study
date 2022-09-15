# -*- coding: utf-8 -*-
import sys

color_map = {
    "R" : {
        "R" : "R", "G" : "Y", "B" : "M",
    },
    "G" : {
        "R" : "Y", "G" : "G", "B" : "C",
    },
    "B" : {
        "R" : "M", "G" : "C", "B" : "B"
    }
}

N, M = map(int, sys.stdin.readline().split())
rows = list(sys.stdin.readlines())
a, b = rows[:N], rows[N:]
a = list(map(lambda r: r.split(), a))
b = list(map(lambda r: r.split(), b))

c = [[[] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        c[i][j] = color_map[a[i][j]][b[i][j]]

print('\n'.join(list(map(lambda x: ' '.join(x), c))))