from sys import stdin
import numpy as np
n,m=map(int, stdin.readline().split())
a=[list(map(str,stdin.readline().split())) for _ in range(n)]
b=[list(map(str,stdin.readline().split())) for _ in range(n)]
c=np.eye(n,m,dtype=str)
for i in range(n):
    for j in range(m):
        if a[i][j]=='R':
            if b[i][j]=='R':
                c[i][j] = 'R'
            elif b[i][j]=='G':
                c[i][j] = 'Y'
            else:
                c[i][j]='M'
        elif a[i][j]=='G':
            if b[i][j]=='R':
                c[i][j] = 'Y'
            elif b[i][j]=='G':
                c[i][j] = 'G'
            else:
                c[i][j]='C'
        else:
            if b[i][j]=='R':
                c[i][j] = 'M'
            elif b[i][j]=='G':
                c[i][j] = 'C'
            else:
                c[i][j]='B'
for i in range(n):
    for j in range(m):
        print(c[i][j], end=" ")
    print("")