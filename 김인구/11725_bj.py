import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n+1)]

parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(s, t, p):
    for i in t[s]:
        if p[i] == 0:
            p[i] = s
            dfs(i, t, p)
            
dfs(1, tree, parent)

for i in range(2, n+1):
    print(parent[i])