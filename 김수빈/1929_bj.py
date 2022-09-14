import sys

def search_prime_num(N, M):
    flags = [0, 0] + [1 for _ in range(2, N + 1)]
    for i in range(2, N + 1):
        for j in range(2 * i, N + 1, i):
            flags[j] = 0
    return list(filter(lambda x: flags[x] ==  1, range(M, N + 1)))


M, N = map(int, sys.stdin.readline().split())
for n in search_prime_num(N, M):
    print(n)