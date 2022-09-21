import sys

sys.setrecursionlimit(10 ** 9)

# 방향 그래프 인접 행렬이 주어지고 
# i에서 j까지의 경로가 존재하는지 판별 -> DFS
def search_dfs(N, board, visited, i, j):
    visited[i] = True
    if board[i][j] == 1: return True
    neighbors = list(filter(lambda x: board[i][x] == 1, range(N)))
    for n in neighbors:
        if visited[n]: continue
        if search_dfs(N, board, visited, n, j):
            return True
    return False

N = int(sys.stdin.readline())
board = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

answer = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        visited = [False] * N
        answer[i][j] = int(search_dfs(N, board, visited, i, j))
    print(' '.join(list(map(str, answer[i]))))