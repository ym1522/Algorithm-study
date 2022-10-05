# -*- coding: utf-8 -*-
import sys
from functools import reduce

input_str = sys.stdin.readline().strip()
claps = [1 if x in '369' else 0 for x in input_str]
n = reduce(lambda x, y: x + y, claps)
print('clap' * n) if n > 0 else print(input_str)