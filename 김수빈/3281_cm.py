import sys

N, K = map(int, sys.stdin.readline().split())
earnings = list(map(int, sys.stdin.readline().split()))

max_earning = 0
for i in range(N - K + 1):
    if 0 in earnings[i:i + K]: continue
    earning = sum(earnings[i:i + K])
    max_earning = earning if earning > max_earning else max_earning
print(max_earning)