import sys

n, m = map(int, sys.stdin.readline().split(' '))
a = []; b=[]; res=[]

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split(' '))))
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split(' '))))

for i in range(n):
    for j in range(m):
        res = (a[i][j]+b[i][j])
        print(res, end=' ')
    print()