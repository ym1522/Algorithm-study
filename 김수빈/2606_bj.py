import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))

root = 1
neighbors = list(filter(lambda x: root in x, edges))
neighbors = list(map(lambda x: x[1] if x[0] == root else x[0],  neighbors))

visited = [root]

while neighbors:
    n = neighbors[0]
    neighbors = neighbors[1:]

    visited += [n]
    nxt_neighbors = list(filter(lambda x: n in x, edges))
    nxt_neighbors = list(map(lambda x: x[0] if n == x[1] else x[1], nxt_neighbors))

    nxt_neigbors = list(filter(lambda x: not x in visited and not x in neighbors, nxt_neighbors))

    neighbors += nxt_neigbors

print(len(visited) - 1)