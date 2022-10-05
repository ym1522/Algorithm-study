import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
cnt = 0

s, e = 0, 0
while e < n:
    temp = sum(arr[s:e+1])
    if temp > k:
        cnt += 1
        s += 1
    else:
        e += 1

print(cnt)

## 못풀음