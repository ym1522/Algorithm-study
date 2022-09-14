from sys import stdin
from collections import deque

a=stdin.readline().strip()
b=stdin.readline().strip()
ch=0
a=deque(a)
b=deque(b)
for i in range(0,len(a)):
    b.rotate(1)
    #print(b)
    if a == b:
        ch=1
        break
    else:
        ch=0
if ch==1:
    print('YES')
else:
    print('NO')