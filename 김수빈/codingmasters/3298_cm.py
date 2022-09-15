# -*- coding: utf-8 -*-
import sys

h, m, s = map(int, sys.stdin.readline().split(':'))
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())

times = h * 3600 + m * 60 + s + (n - 1) * t
h, times = (times // 3600) % 24, times % 3600
m, times = times // 60, times % 60
s = times

print("%02d:%02d:%02d" % (h, m, s))