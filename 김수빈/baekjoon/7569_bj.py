import sys
from collections import deque

def solution(H, N, M, board, coord):
    max_k, max_i, max_j = 0, 0, 0
    while coord:
        k, i, j = coord.popleft()
        neighbors = [(k - 1, i, j), (k + 1, i, j), (k, i - 1, j), (k, i + 1, j), (k, i, j - 1), (k, i, j + 1)]
        for n_k, n_i, n_j  in neighbors:
            if n_k < 0 or n_i < 0 or n_j < 0 or n_k >= H or n_i >= N or n_j >= M: continue
            if board[n_k][n_i][n_j] == 0 or board[n_k][n_i][n_j] > board[k][i][j] + 1:
                board[n_k][n_i][n_j] = board[k][i][j] + 1
                coord.append((n_k, n_i, n_j))
                if board[n_k][n_i][n_j] > board[max_k][max_i][max_j]:
                    max_k, max_i, max_j = n_k, n_i, n_j
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if board[k][i][j] == 0: return -1
    return board[max_k][max_i][max_j] - 1

M, N, H = map(int, sys.stdin.readline().split())
board = []
for _ in range(H):
    sub_board = []
    for _ in range(N):
        sub_board += [list(map(int, sys.stdin.readline().split()))]
    board += [sub_board]
    
coord = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if board[k][i][j] == 1:
                coord.append((k, i, j))
print(solution(H, N, M, board, coord))
