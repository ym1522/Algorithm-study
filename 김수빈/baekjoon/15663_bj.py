import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

def search_dfs(N, M, nums, cnt, seq, seq_id):
    if cnt == M:
        return [' '.join(seq)]

    answer = []
    for j in range(N):
        if j in seq_id: continue
        answer += search_dfs(N, M, nums, cnt + 1, seq + [f'{nums[j]}'], seq_id + [j])
    return answer

answer = search_dfs(N, M, nums, 0, [], [])
# answer 내 중복 수열 제거 및 정렬 

answer = list(set(answer))
answer = sorted(answer, key=lambda x: tuple(map(int, x.split())))

# 개별로 출력하면 시간초과
print('\n'.join(answer))