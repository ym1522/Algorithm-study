# -*- coding: utf-8 -*-
import sys
from functools import reduce

N = int(sys.stdin.readline())
problems = list(map(int, sys.stdin.readline().split()))

left = 100 - reduce(lambda x, y: x + y, problems)
print(max(left, 0))