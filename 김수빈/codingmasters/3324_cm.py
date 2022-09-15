import sys
from functools import reduce

def dfs(D, K, edges, visited, limits, v):
    visited += [v]

    neighbors = list(filter(lambda x: v in x, edges))
    neighbors = list(map(lambda x: x[0] if x[1] == v else x[1], neighbors))
    neighbors = list(filter(lambda x: not x in visited, neighbors))

    if not neighbors:
        if limits[v][0] <= D[v]:
            limits[v] = (D[v], max(D[v], limits[v][1]))
        return limits, visited
    
    for n in neighbors:
        limits[n] = (limits[v][0] - K, limits[v][0])
        limits, visited = dfs(D, K, edges, visited, limits, n)
        if limits[n][0] - limits[v][0] > K:
            limits[v] = (limits[n][0] - K, limits[v][1])
    return limits, visited
    
N, M, K = map(int, sys.stdin.readline().split())
edges = []
D = {}
for i in range(N):
    s = int(sys.stdin.readline())
    D[i + 1] = s

for _ in range(M):
    edges += [tuple(map(int, sys.stdin.readline().split()))]

visited = []
to_visit = list(set(reduce(lambda x, y: x + y, edges)))
nodes = list(filter(lambda x: x[0] in to_visit, D.items()))
nodes = sorted(nodes, key=lambda x: x[-1], reverse=True)

total_cost = 0
while nodes:
    v, s = nodes[0]
    limits, visited = dfs(D, K, edges, visited, {v : (s, s)}, v)
    for v in limits.keys():
        total_cost += max(limits[v][0], D[v]) - D[v]
    nodes = list(filter(lambda x: not x[0] in visited, nodes))
print(total_cost)