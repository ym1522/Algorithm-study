# 동전 0 

import sys
n, k = map(int, sys.stdin.readline().split())
res = 0

a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in reversed(range(len(a))):
    if k == 0 : break
    res += k // a[i][0]
    k = k % a[i][0]
    
print(res)