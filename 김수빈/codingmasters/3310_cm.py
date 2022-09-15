import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())
board = list(map(lambda x: list(map(int, x.strip())), sys.stdin.readlines()))
board = np.array(board)
S = set()
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for x in range(N - i + 1):
            for y in range(M - j + 1):
                if not 0 in board[x:x + i, y:y + j]:
                    S.add((x, y, i, j))            
print(len(S))