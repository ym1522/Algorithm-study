# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
basket = list(map(lambda x: tuple(map(int, x.split())), sys.stdin.readlines()))
comp_basket = list(map(lambda x: (x[0], (-x[1][0], x[1][1], x[1][2])), enumerate(basket)))
comp_basket = sorted(comp_basket, key=lambda x: x[-1])

for i, _ in comp_basket:
    print(i + 1, end=' ')