# -*- coding: utf-8 -*-
import sys

K = int(sys.stdin.readline())
N = K + 2 if K % 2 == 0 else K + 1
while True:
    if (N // 2) % 2 == 1:
        print(N)
        break
    N += 2