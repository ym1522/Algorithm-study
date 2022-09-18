# -*- coding: utf-8 -*-
import sys

x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())
dist = (r1 + r2)/2
print("YES") if abs(x1 - x2) <= dist and abs(y1 - y2) <= dist else print("NO")