import sys

def dfs(target, n, visited, edges):
    if n == target: return 0

    visited[n - 1] = 1
    n_neighbors = list(filter(lambda x: n in x, edges))
    n_neighbors = list(map(lambda x: x[0] if x[1] == n else x[1], n_neighbors))
    n_neighbors = list(filter(lambda x: visited[x - 1] == 0, n_neighbors))
    
    min_depth = -1
    for nxt_n in n_neighbors:
        depth = dfs(target, nxt_n, visited, edges)
        if depth < 0: continue
        min_depth = depth + 1 if min_depth < 0 or depth + 1 < min_depth else min_depth
    
    return min_depth 
    
N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
edges = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))
visited = [0] * N
print(dfs(B, A, visited, edges))