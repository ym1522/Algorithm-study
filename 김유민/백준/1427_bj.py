# 1427 - 소트인사이드

import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
print(*n, sep='')