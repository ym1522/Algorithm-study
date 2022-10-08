import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip()))

res = 0
for i in arr:
    res += i

print(res)