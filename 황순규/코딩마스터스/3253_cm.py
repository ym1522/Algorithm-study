import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.remove(max(nums))
print(int(nums[0] * nums[1] / 2))