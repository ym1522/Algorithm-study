import sys
from collections import deque

n = int(sys.stdin.readline())
MyDeque = deque()

for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == 'push_front': MyDeque.appendleft(int(s[1]))
    if s[0] == 'push_back': MyDeque.append(int(s[1]))
    if s[0] == 'pop_front': 
        try: print(MyDeque.popleft())
        except IndexError: print(-1)
    if s[0] == 'pop_back': 
        try: print(MyDeque.pop())
        except IndexError: print(-1)
    if s[0] == 'size': print(len(MyDeque))
    if s[0] == 'empty': print(1 if len(MyDeque)==0 else 0)
    if s[0] == 'front': 
        try: print(MyDeque[0])
        except IndexError: print(-1)
    if s[0] == 'back': 
        try: print(MyDeque[-1])
        except IndexError: print(-1)