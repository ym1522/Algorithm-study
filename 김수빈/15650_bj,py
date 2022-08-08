import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cases = list(combinations(list(range(1, N + 1)), M))
cases.sort()
for case in cases:
    print(' '.join(list(map(str, case))))