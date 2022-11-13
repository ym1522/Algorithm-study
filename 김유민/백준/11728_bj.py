# 배열 합치기
# 메모리: 184460KB, 시간: 1552ms

import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = a+b
res.sort()

print(*res)