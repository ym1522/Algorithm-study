import sys
from functools import reduce

def solution(board, N, M, B):
    values = list(reduce(lambda x, y: x + y, board))
    current = sum(values) + B
    min_time, height = None, None

    cnt = N * M 
    for h in range(min(values), min(max(values), 256) + 1):
        if h * cnt > current: break 
        time = 0
        for v in values:
            if v > h: time += 2 * (v - h)
            elif v < h: time += 1 * (h - v)
        if min_time is None or time < min_time or (time == min_time and height < h):
            min_time, height = time, h
    return min_time, height

N, M, B = map(int, sys.stdin.readline().split())
board = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
time, h = solution(board, N, M, B)
print(f"{time} {h}")
