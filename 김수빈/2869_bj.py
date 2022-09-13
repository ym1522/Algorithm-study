import sys

def solution(A, B, V):
    day = ((V - A) / (A - B)) + 1
    point = day - int(day)
    if day == int(day): return int(day)
    return int(day + 1)

A, B, V = map(int, sys.stdin.readline().split())

print(solution(A, B, V))
