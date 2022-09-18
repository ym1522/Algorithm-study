import sys

sys.setrecursionlimit(10**6)
def search_dfs(i, j, board, h, w, visited):
    if visited[i][j] == 1: return visited

    visited[i][j] = 1
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), 
                 (i - 1, j + 1), (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1)]
    neighbors= list(filter(lambda x: x[0] >= 0 and x[0] < h and x[1] >= 0 and x[1] < w, neighbors))
    neighbors = list(filter(lambda x: visited[x[0]][x[1]] == 0 and board[x[0]][x[1]] == 1, neighbors))

    for n_i, n_j in neighbors:   
        visited = search_dfs(n_i, n_j, board, h, w, visited)
    return visited


def solution(h, w, board):
    visited = [[0 for j in range(w + 1)] for i in range(h + 1)]
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == 0:
                visited = search_dfs(i, j, board, h, w, visited)
                count += 1
    return count

w, h = map(int, sys.stdin.readline().split())
while (w, h) != (0, 0):
    board = []
    for i in range(h):
        board += [list(map(int, sys.stdin.readline().split()))]
    print(solution(h, w, board))    
    w, h = map(int, sys.stdin.readline().split())

    