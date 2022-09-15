# -*- coding: utf-8 -*-
import sys, math

a, b, D, d = map(int, sys.stdin.readline().split())

min_n = 2 * (math.ceil(a / D) - 1) + 2 * (math.ceil(b / D) - 1) + 4
max_n = 2 * (a // d - 1) + 2 * (b // d - 1) + 4
print(f"{min_n} {max_n}") if d <= a and d <= b else print(-1)