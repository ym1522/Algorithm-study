# -*- coding: utf-8 -*-
import sys

def is_possible(x, y, i, j):
    cases = [(x, y)]
    prev = []
    while cases:
        x, y = cases.pop()
        prev += [(x, y)]
        if (x, y) == (i, j): return True

        for t, u in [(x-1, y+2), (x+1, y+2), (x-2, y+1), (x-2, y-1), (x+2, y-1), (x+2, y+1), (x-1, y-2), (x+1, y-2)]:
            if t < 0 or u < 0 or t >= 3 or u >= 3 or (t, u) in prev: continue
            cases += [(t, u)]
    return False
    
def solution(white, black):
    if is_possible(*white[0], *black[0]) and is_possible(*white[1], *black[1]):
        return True
    elif is_possible(*white[0], *black[1]) and is_possible(*white[1], *black[0]):
        return True
    return False

board = list(map(lambda x: list(map(int, x.strip())), sys.stdin.readlines()))
white, black = [], []
for i in range(3):
    for j in range(3):
        if board[i][j] == 1:
            white += [(i, j)]
        elif board[i][j] == 2:
            black += [(i, j)]

print("possible") if solution(white, black) else print("impossible")