
def search_dfs(V, N, visited, edges):
    if not V in visited:
        visited += [V]

    if len(visited) >= N:
        return visited[:N]

    possibles = list(filter(lambda x: x[0] == V or x[1] == V, edges))
    possibles = list(map(lambda x: x[1] if x[0] == V else x[0], possibles))
    possibles = list(filter(lambda x: not x in visited, possibles))

    if not possibles: return visited
    possibles.sort()
    
    for next in possibles:
        visited = search_dfs(next, N, visited, edges)

    return visited 

def search_bfs(V, N, edges):
    cases = [V]
    visited = []
    
    prev_nodes = []
    while cases:
        node = cases[0]
        cases = cases[1:]
        if not node in visited:
            visited += [node]

        if node in prev_nodes: continue
        prev_nodes += [node]

        if len(visited) >= N:
            return visited[:N]

        possibles = list(filter(lambda x: x[0] == node or x[1] == node, edges))
        possibles = list(map(lambda x: x[1] if x[0] == node else x[0], possibles))
        possibles = list(filter(lambda x: not x in visited, possibles))
        possibles.sort()

        if not possibles: continue
        
        for next in possibles:
            cases += [next]
    return visited

N, M, V = map(int, input().split())

edges = []
for i in range(M):
    n_1, n_2 = map(int, input().split())
    edges += [(n_1, n_2)]

print(' '.join(map(str, search_dfs(V, N, [], edges))))
print(' '.join(map(str, search_bfs(V, N, edges))))
