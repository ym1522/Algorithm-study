import sys

def DFS(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i , visited)

coms = int(sys.stdin.readline())
N = int(sys.stdin.readline())

all_coms = [[] for i in range(coms + 1)]
visited = [False] * (coms + 1)

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    all_coms[a].append(b)
    all_coms[b].append(a)

DFS(all_coms, 1, visited)

cnt = 0
for i in visited:
    if i == True:
        cnt += 1

if cnt == 0:
    print(cnt)
else:
    print(cnt - 1)