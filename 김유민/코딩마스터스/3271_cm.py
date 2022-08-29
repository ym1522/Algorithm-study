import sys

n = int(sys.stdin.readline())
arr = []

arr = list(map(int, (sys.stdin.readline()).split()))
res = 100 - sum(arr)

if sum(arr) >= 100: print(0)
else: print(res)