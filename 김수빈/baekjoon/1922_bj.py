import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

# Union-Find
def get_parent(nodes, n):
    if n == nodes[n - 1]: return n
    return get_parent(nodes, nodes[n - 1])

cost = 0
nodes = [u for u in range(1, N + 1)]

# Kruskal Algorithm
edges = sorted(edges, key=lambda x: x[-1])
for u, v, w in edges:
    par_u = get_parent(nodes, u)
    par_v = get_parent(nodes, v)

    if par_u == par_v: continue 
    cost += w

    if par_u < par_v:
        nodes[par_v - 1] = par_u
    else:
        nodes[par_u - 1] = par_v
print(cost)