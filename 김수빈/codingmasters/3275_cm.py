# -*- coding: utf-8 -*-
import sys

input_str = sys.stdin.readline().strip()
A = list(map(lambda x: ord(x), input_str))
i = 0
while i < len(A):
    if A[i] in [34, 39, 92]:
        A = A[:i] + [92] + A[i:]
        i += 1
    i += 1

print(''.join(list(map(lambda x: chr(x), A))))