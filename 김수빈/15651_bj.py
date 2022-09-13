import sys

def search_dfs(M, cur, left):
    if len(cur) == M: return [cur]

    cases = []
    for i, n in enumerate(left):
        cases += search_dfs(M, cur + [n], left)
    return cases

N, M = map(int, sys.stdin.readline().split())
nums = list(range(1, N + 1))
cases = search_dfs(M, [], nums)

cases.sort()

answer = []
for c in cases:
    answer += [' '.join(list(map(str, c)))]
print("\n".join(answer))