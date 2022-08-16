import sys

n, m = map(int, sys.stdin.readline().split())
res = (n-1) + n*(m-1)
print(res)