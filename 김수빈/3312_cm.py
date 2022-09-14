# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
seqs = [nums[i:i+3] for i in range(N - 2)]
for seq in seqs:
    seq.remove(min(seq))
    seq.remove(max(seq))
    result = seq[0] if seq[0] > result else result

print(result)