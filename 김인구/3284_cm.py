import sys
from collections import deque

q = deque([0])

a = int(sys.stdin.readline())
for i in range(1, a+1):
    card = sys.stdin.readline().strip()
    if card == "D":
        q.appendleft(i)
    else:
        q.append(i)
        
while q:
    print(q.popleft(), end = " ")