import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

ans = 100 - sum(num)

if ans < 0:
    print(0)
else:
    print(ans)