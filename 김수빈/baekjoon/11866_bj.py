import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(range(1, N + 1))
answer = []
idx = (K - 1) % N
while nums:
    answer += [str(nums[idx])]
    nums = nums[:idx] + nums[idx + 1:]
    idx = (idx + K - 1) % len(nums) if len(nums) > 0 else 0

print("<" + ', '.join(answer) + ">")