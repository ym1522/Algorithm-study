import sys

def solution(n, m):
    if n == 1 and m == 1: return 0
    elif n == 1:
        return 1 + solution(n, m // 2) + solution(n, m - m //2)
    return 1 + solution(n // 2, m) + solution(n - n //2, m)
    
N, M = map(int, sys.stdin.readline().split())
print(solution(N, M))