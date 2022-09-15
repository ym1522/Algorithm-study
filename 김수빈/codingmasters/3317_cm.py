# -*- coding: utf-8 -*-
import sys
from functools import reduce

N = int(sys.stdin.readline())
arr = list(sys.stdin.readlines())
arr = list(map(lambda x: list(x.split()) , arr))

for i in range(N):
    if not '1' in arr[i]:
        arr[i] = ['0'] * N
    
    if not '1' in [arr[j][i] for j in range(N)]:
        for j in range(N):
            arr[j][i] = '0'

print(reduce(lambda x, y: x + y, arr).count('2'))