import sys

N, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse = True)

cnt = 0
for c in coins:
    cnt += k // c
    k %= c
    
print(cnt) 
