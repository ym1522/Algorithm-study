import sys

nums = list(map(int, sys.stdin.readlines()))
i = 0
while i < len(nums):
    n = nums[i]
    sum_val = sum(nums[i + 1:i + 1 + n])
    sign = '+' if sum_val > 0 else str(sum_val)
    sign = '-' if sum_val < 0 else sign
    print(sign)
    i = i + n + 1