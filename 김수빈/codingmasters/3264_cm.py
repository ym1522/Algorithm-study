# -*- coding: utf-8 -*-
import sys

A, B, C = map(int, sys.stdin.readline().split())
if A ** 2 > C * (B ** 2):
    print("NO")
else:
    print("YES")