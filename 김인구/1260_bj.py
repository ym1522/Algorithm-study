import sys
from collections import deque

input = sys.stdin.readline

# 정점, 간선, 시작점
n, m, v = map(int, input().split())

# 그래프
graph = [[] for _ in range(n+1)]
# graph = [[0]*(n+1) for _ in range(n+1)]

# dfs, bfs 방문확인용
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

# 그래프 양방향 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    #graph[a][b] = graph[b][a] = 1

# 작은 정점 먼저 방문하기 위해 정렬
for i in range(len(graph)):
    graph[i].sort()

# dfs
def dfs(v):
    
    # 방문 처리
    visited1[v] = True
    print(v, end=' ')
    
    # 정점과 연결된 정점 찾아 접근
    for i in graph[v]:
        if not visited1[i]:
            dfs(i)

# bfs
def bfs(v):
    q = deque([v])
    
    #첫방문 방문처리
    visited2[v] = True
    
    # 큐 빌때까지 반복
    while q:
        
        #가장 먼저들어온 정점 큐에서 빼기
        now = q.popleft()
        print(now, end=' ')
        
        # 그 정점과 연결된 정점들의 방문확인하여 큐에 넣기
        for i in graph[now]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True

dfs(v)
print("")
bfs(v)