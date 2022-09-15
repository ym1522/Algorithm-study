# -*- coding: utf-8 -*-
import sys

def is_prime(N):
    if N <= 1: return False
    if N == 2: return True
    for i in range(2, N - 1):
        if N % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
print("clap") if is_prime(N) else print(N)

