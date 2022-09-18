# -*- coding: utf-8 -*-
import sys
from itertools import permutations

def solution(nums):
    for n in nums:
        if n % 13 == 0: 
            return "YES"
    return "NO"

input_num = sys.stdin.readline().strip()
nums = list(map(lambda x: int(''.join(x)), list(permutations(input_num, len(input_num)))))

print(solution(nums))        