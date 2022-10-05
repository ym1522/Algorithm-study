import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

def solution(A, B):
    # BFS로 접근
    cases = deque([(A, 0)])

    min_cnt = -1
    while cases:
        a, cnt = cases.popleft()
        if a == B:
            min_cnt = cnt + 1 if min_cnt < 0 or min_cnt > cnt + 1 else min_cnt

        a_1 = a * 2
        a_2 = int(f"{a}1")
        if a_1 <= B:
            cases.append((a_1, cnt + 1))
        if a_2 <= B:
            cases.append((a_2, cnt + 1))
    return min_cnt
print(solution(A, B))