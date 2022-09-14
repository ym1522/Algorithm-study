import sys

def dfs(edges, node):
    if node == 1: return True

    nxt_indices = list(filter(lambda x: edges[x][0] == node, range(len(edges))))
    for i in nxt_indices:
        if dfs(edges[:i] + edges[i + 1:], edges[i][1]): return True
    return False
    
N, M = map(int, sys.stdin.readline().split())
edges = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

answer = "NO"
nxt_indices = list(filter(lambda x: edges[x][0] == 1, range(len(edges))))
for i in nxt_indices:
    if dfs(edges[:i] + edges[i + 1:], edges[i][1]):
        answer = "YES"
        break

print(answer)