import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

# 양방향 그래프 구축
graph = {i: deque() for i in range(1, N + 1)}
for u, v in edges:
    graph[u].append((u, v))
    graph[v].append((v, u))
visited = [False] * N

# 상근이의 친구 탐색
neighbors = graph[1].copy()
neighbors_2 = deque()
visited[0] = True

while neighbors:
    u, v = neighbors.popleft()
    visited[v - 1] = True

    for _, n in graph[v]:
        if visited[n - 1]: continue
        neighbors_2.append((v, n))
        
# 상근이의 친구의 친구 탐색    
while neighbors_2:
    u, v = neighbors_2.popleft()
    visited[v - 1] = True
        
print(len(list(filter(lambda x: visited[x], range(N)))) - 1)