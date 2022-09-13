import sys

def search_dfs(cur, tgt, left):
    if not left:
        return 1 if cur == tgt else -1

    result = 0 if cur != tgt else 1
    for i, n in enumerate(left):
        cnt = search_dfs(cur + n, tgt, left[i + 1:])
        if cnt < 0: continue
        result += cnt
        
    return result

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
for i, n in enumerate(nums):
    cnt = search_dfs(n, S, nums[i + 1:])
    if cnt < 0: continue
    result += cnt
print(result)
