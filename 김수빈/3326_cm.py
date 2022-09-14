import sys
from itertools import combinations

def swap_node(u, v, E):
    new_E = []
    for i, j in E:
        if i in [u, v]:
            i = u if i == v else v
        if j in [u, v]:
            j = u if j == v else v
        new_E += [(min(i, j), max(i, j))]
    return new_E

def solution_bfs(N, E_1, E_2):
    cases = [(E_1, [])]
    while cases:
        E, swapped = cases.pop()
        if set(E_2) == set(E): return "YES"
        left = list(filter(lambda x: not x in swapped, range(1, N + 1)))
        for i, j in list(combinations(left, 2)):            
            new_E = swap_node(i, j, E)
            cases += [(new_E, swapped + [i])]
    return "NO"

N_1, M_1 = map(int, sys.stdin.readline().split())
E_1, E_2 = [], []
for _ in range(M_1):
    E_1 += [tuple(map(int, sys.stdin.readline().split()))]

N_2, M_2 = map(int, sys.stdin.readline().split())
for _ in range(M_2):
    E_2 += [tuple(map(int, sys.stdin.readline().split()))]   

E_1 = list(map(lambda x: (x[1], x[0]) if x[0] > x[1] else x, E_1))
E_2 = list(map(lambda x: (x[1], x[0]) if x[0] > x[1] else x, E_2))

print(solution_bfs(N_1, E_1, E_2))