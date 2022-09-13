# -*- coding: utf-8 -*-
import sys
import copy

board = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
N = len(board)
answer = list(map(lambda x: list(map(str, range(x * N + 1, x * N + 1 + N))), range(N)))
answer[-1][-1] = "X"
get_key = lambda x: ''.join(list(map(lambda k: ''.join(k), x)))


def dfs(board, N, x, y, visited, recur):
    global answer
    if board == answer: return 0
    key = get_key(board)
    
    if key in visited:
        visited[key] = recur if visited[key] > recur else visited[key]
    else:
        visited[key] = recur

    k = -1
    if x > 0:
        new_board = copy.deepcopy(board)
        new_board[x][y], new_board[x - 1][y] = new_board[x - 1][y], new_board[x][y]
        key = get_key(new_board)
        if not key in visited or visited[key] > recur:
            new_k = dfs(new_board, N, x - 1, y, visited, recur + 1)
            if new_k >= 0: 
                k = new_k + 1 if new_k + 1 < k or k < 0 else k

    if x < N - 1:
        new_board = copy.deepcopy(board)
        new_board[x][y], new_board[x + 1][y] = new_board[x + 1][y], new_board[x][y]
        key = get_key(new_board)
        if not key in visited or visited[key] > recur:
            new_k = dfs(new_board, N, x + 1, y, visited, recur + 1)
            if new_k >= 0: 
                k = new_k + 1 if new_k + 1 < k or k < 0 else k
    if y > 0:
        new_board = copy.deepcopy(board)
        new_board[x][y], new_board[x][y - 1] = new_board[x][y - 1], new_board[x][y]
        key = get_key(new_board)
        if not key in visited or visited[key] > recur:
            new_k = dfs(new_board, N, x, y - 1, visited, recur + 1)
            if new_k >= 0: 
                k = new_k + 1 if new_k + 1 < k or k < 0 else k

    if y < N - 1:
        new_board = copy.deepcopy(board)
        new_board[x][y], new_board[x][y + 1] = new_board[x][y + 1], new_board[x][y]
        key = get_key(new_board)
        if not key in visited or visited[key] > recur:
            new_k = dfs(new_board, N, x, y + 1, visited, recur + 1)
            if new_k >= 0: 
                k = new_k + 1 if new_k + 1 < k or k < 0 else k
    return k
    
x, y = -1, -1
for i in range(N):
    if 'X' in board[i]:
        x, y = i, board[i].index('X')
        break

print(dfs(board, N, x, y, {}, 0))