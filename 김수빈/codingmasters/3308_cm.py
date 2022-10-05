# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
max_area = 0
for i in range(N):
    area = i * (N // 2 - i)
    max_area = area if area > max_area else max_area
print(max_area)