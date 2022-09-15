# -*- coding: utf-8 -*-
import sys

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
D = int(sys.stdin.readline())
today = sys.stdin.readline().strip()
print(day[(D % 7 + day.index(today)) % 7])