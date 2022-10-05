import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

def search_dfs(N, M, nums, i, cnt, seq, seq_id):
    if cnt == M:
        return [' '.join(seq)]

    answer = []
    for j in range(i, N):
        answer += search_dfs(N, M, nums, j, cnt + 1, seq + [f'{nums[j]}'], seq_id + [j])
    return answer

answer = search_dfs(N, M, nums, 0, 0, [], [])
answer = list(set(answer))
answer = sorted(answer, key=lambda x: tuple(map(int, x.split())))


print('\n'.join(answer))