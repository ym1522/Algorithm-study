from sys import stdin
from collections import deque

def dfs(start, num):
    num+=1
    visited[start]=True
    if start==y:
        co.append(num)
    for i in graph[start]:
        if not visited[i]:
            dfs(i,num)    
    

n=int(stdin.readline())
x, y = map(int,stdin.readline().split())
m = int(stdin.readline())
visited=[False]*(n+1)
co=[]
graph=[[]*n for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(x,0)
if len(co)==0:
    print(-1)
else:
    print(co[0]-1)