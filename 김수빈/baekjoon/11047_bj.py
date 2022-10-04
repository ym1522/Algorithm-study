import sys

N, K = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readlines()))

cnt = 0
cur = K
for c in coins[::-1]:
    cnt += (cur // c)
    cur -= (cur // c) * c
    if cur == 0: break
    
print(cnt)