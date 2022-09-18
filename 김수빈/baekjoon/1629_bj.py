import sys

A, B, C = map(int, sys.stdin.readline().split())
leaf = A % C
def solution(A, n, C):
    if n == 1: return leaf

    half = n // 2
    remain = solution(A, half, C)
    if half == n - half: 
        return (remain ** 2) % C
    
    return (remain * remain * A) % C

print(solution(A, B, C))