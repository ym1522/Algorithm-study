# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums = list(filter(lambda x: nums.count(x) >= 2, nums))

try:
    max_w = max(nums)
    nums.remove(max_w)
    nums.remove(max_w)
    print(max_w * max(nums))
except:
    print(0)