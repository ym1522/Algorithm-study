# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
secs = 12 * 60 * 60 - N

min, sec = secs // 60, secs % 60
h, min = min // 60, min % 60
print(f"%02d:%02d:%02d" % (h, min, sec))