# -*- coding: utf-8 -*-
import sys

scores = list(map(int, sys.stdin.readline().split()))
fails = list(filter(lambda x: x < 40, scores))
if sum(scores) / len(scores) >= 60 and not fails:
    print("P")
else:
    print("F")