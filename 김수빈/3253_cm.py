# -*- coding: utf-8 -*-
import sys
a, b, c = map(int, sys.stdin.readline().split())
if a ** 2 + b ** 2 == c ** 2:
    print(a * b // 2)
elif a ** 2 + c ** 2 == b ** 2:
    print(a * c // 2)
else:
    print(b * c // 2)