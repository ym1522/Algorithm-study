# 거스름돈

import sys

pay = int(sys.stdin.readline())
change = 1000 - pay
res = 0

coin = [500, 100, 50, 10, 5, 1]

for i in coin:
    res += change // i
    change %= i

print(res)