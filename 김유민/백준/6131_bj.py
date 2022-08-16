# 완전 제곱수 -

import sys

n = int(sys.stdin.readline())
count = 0

for b in range(1, 501):
    for a in range(b, 501):
        if a**2 == (n + b**2):
            count += 1
print(count)