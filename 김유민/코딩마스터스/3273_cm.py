import sys

n = int(sys.stdin.readline())
res = [n, ]

while True:
    if n % 2 == 0:
        res.append(n//2)
        n = n//2
    else:
        res.append(3*n+1)
        n = 3*n+1
        
    if n == 1:
        break

for i in res:
    print(i, end=' ')