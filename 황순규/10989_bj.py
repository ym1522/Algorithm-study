import sys

N = int(sys.stdin.readline())
nums = [0] * N

for i in range(N):
    nums[i] = int(sys.stdin.readline())

nums.sort()

for i in nums:
    print(i)