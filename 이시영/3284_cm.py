from sys import stdin
from collections import deque

n=int(stdin.readline())
a=deque()
a.append(0)
for i in range(1,n+1):
    z=input()
    if z=='U':
        a.append(i)
    elif z=='D':
        a.appendleft(i)
for i in range(n+1):
    print(a[i], end=" ")