import sys
from itertools import product

def solution(N):
    if N == 1: return 666
    base = "666"
    rank = N - 2

    n_digits = 1
    while rank >= 0:
        cands = []
        for pre, su in list(map(lambda x: (x, n_digits - x), range(n_digits + 1))):
            prefixs = list(range(10 ** (pre - 1), 10 ** pre)) if pre > 0 else ['']
            suffixs = list(map(lambda x: f"%0{su}d" % x, range(10 ** su))) if su > 0 else ['']
            cands += list(map(lambda x: str(x[0]) + base + str(x[1]), list(product(prefixs, suffixs))))
        cands = list(set(cands))
        cands.sort()
        if len(cands) > rank:
            return int(cands[rank])
        rank -= len(cands)
        n_digits += 1
    return -1
N = int(sys.stdin.readline())
print(solution(N))