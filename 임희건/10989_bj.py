# 도움주신 수빈님, 유민님, 시영님 감사합니다 (__)

import sys

N = int(sys.stdin.readline())
list = [0] * 10001

for i in range(N):
    n = int(sys.stdin.readline())
    list[n] += 1

for j in range(10001):
    if j != 0:
        for k in range(list[j]):
            print(j)