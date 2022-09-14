from sys import stdin
from collections import deque

def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

n = int(stdin.readline())
k = int(stdin.readline())
graph=[[]*n for _ in range(n+1)]
for _ in range(k):
    a, b = map(int,stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
count=dfs(graph, 1)
print(len(count)-1)
