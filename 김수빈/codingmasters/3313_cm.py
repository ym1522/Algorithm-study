# -*- coding: utf-8 -*-
import sys

nums = list(map(int, sys.stdin.readline().strip()))
nums.sort()

if nums[0] + nums[-1] == nums[1] + nums[2]:
    print("YES")
else:
    print("NO")