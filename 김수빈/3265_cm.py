# -*- coding: utf-8 -*-
import sys

A, B = map(int, sys.stdin.readline().split())
forward = B - A if B >= A else B + 60 - A
back = A - B if A >= B else A + 60 - B 
print(min(forward, back))