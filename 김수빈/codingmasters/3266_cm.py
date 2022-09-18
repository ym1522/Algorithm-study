# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readlines()))
for n in nums:
    if n % 2 == 0: print("R")
    else: print("L")