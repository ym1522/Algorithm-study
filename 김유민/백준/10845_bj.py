import sys

n = int(sys.stdin.readline())
MyQueue = []
for i in range(n):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == 'push': MyQueue.append(int(s[1]))
    if s[0] == 'pop': 
        try: print(MyQueue[0]); MyQueue.remove(MyQueue[0])
        except IndexError: print(-1)
    if s[0] == 'size': print(len(MyQueue))
    if s[0] == 'empty': print(1 if len(MyQueue)==0 else 0)
    if s[0] == 'front': 
        try: print(MyQueue[0])
        except IndexError: print(-1)
    if s[0] == 'back': 
        try: print(MyQueue[-1])
        except IndexError: print(-1)