# -*- coding: utf-8 -*-
import sys, re

cell = sys.stdin.readline().strip()
col = re.split('[1-9]+', cell)[0]
row = int(re.split('[A-Z]+', cell)[-1])

left_col = list(map(ord, col))
i = len(left_col) - 1
while left_col[i] - 1 < 65 and i > 0:
    left_col[i] = ord('Z')
    i -= 1
left_col[i] -= 1

left_col = list(filter(lambda x: x >= 65, left_col))
print(f"{''.join(list(map(chr, left_col)))}{row}")
print(f'{col}{row - 1}')
