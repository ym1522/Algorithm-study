import sys

# 딕셔너리 자료구조 사용
N, M = map(int, sys.stdin.readline().split())
monsters = list(map(lambda x: x.strip(), sys.stdin.readlines()))

problems = monsters[N:]
monsters = monsters[:N]

D, D_inv = {}, {}
for i, m in zip(range(1, N + 1), monsters):
    D[str(i)] = m
    D_inv[m] = i

for p in problems:
    if p in D:
        print(D[p])
    else:
        print(D_inv[p])