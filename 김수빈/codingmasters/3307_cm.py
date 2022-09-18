# -*- coding: utf-8 -*-
import sys

def solution(N):
    seqs = [0] * N
    seqs[0] = '1'
    
    for i in range(1, N):
        chars = list(set(seqs[i - 1]))
        chars.sort()
        seqs[i] = ''.join([f"{c}{seqs[i - 1].count(c)}" for c in chars])
    return seqs[-1]  

N = int(sys.stdin.readline())
print(solution(N))