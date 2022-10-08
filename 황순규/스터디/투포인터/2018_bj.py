import sys

n = int(sys.stdin.readline())
t = n // 2 + 1
cnt = 0

s, e = 1, 1
temp = 0
cnt = 0

while e <= t+1:
    if temp >= n:
        temp -= s
        s += 1
    else:
        temp += e
        e += 1
    if temp == n:
        cnt += 1
    print(s,e,temp)
print(cnt+1)

## 못푸음