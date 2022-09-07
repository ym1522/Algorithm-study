import sys

def solution(N, x, y):
    if x == 0: return 0
    X = x if x > 0 else -x
    times = [0] * X
    for i in range(1, X + 1):
        times[i - 1] = ((i ** 2 + N ** 2) ** 0.5)/10 +(((X - i) ** 2 + y ** 2) ** 0.5)/5
    idx = times.index(min(times)) + 1
    return idx if x > 0 else -idx
    
N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

print(solution(N, x, y))