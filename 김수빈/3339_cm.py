import sys
from collections import deque

def solution(N, x_1, y_1, x_2, y_2):
    cases = deque([(0, x_1, y_1, [])])
    count = 0
    while cases:
        n, x, y, visited = cases.popleft()
        visited += [(x, y)]
        if (n, x, y) == (N, x_2, y_2):
            count += 1
            continue
        if n > N: continue
        
        if (not (x + 1, y) in visited):
            cases += [(n + 1, x + 1, y, visited.copy())]
        if (not (x, y + 1) in visited):
            cases += [(n + 1, x, y + 1, visited.copy())]

        if (not (x - 1, y) in visited):
            cases += [(n + 1, x - 1, y, visited.copy())]
        if (not (x, y - 1) in visited):
            cases += [(n + 1, x, y - 1, visited.copy())]
    return count

N = int(sys.stdin.readline())
x_1, y_1 = map(int, sys.stdin.readline().split())
x_2, y_2 = map(int, sys.stdin.readline().split())

print(solution(N, x_1, y_1, x_2, y_2))