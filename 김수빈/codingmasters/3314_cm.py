# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

cnt = 0
while sum(nums) % N != 0:
    cnt += 1
    nums[-1] -= 1
    nums.sort()
    
tgt_val = sum(nums) // N
cnt += sum([n - tgt_val for n in nums if n > tgt_val])
print(cnt)